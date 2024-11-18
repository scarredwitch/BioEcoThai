from flask import Flask, request, jsonify, render_template
from SPARQLWrapper import SPARQLWrapper, JSON
from flask_cors import CORS  # Import the CORS package
import logging
import requests

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Update the SPARQL endpoint URL to match your Fuseki server
SPARQL_ENDPOINT = "http://localhost:3030/ds/query"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['GET'])
def search():
    term = request.args.get('term')
    if not term:
        return jsonify({"results": []})

    sparql = SPARQLWrapper(SPARQL_ENDPOINT)
    # Basic SPARQL query format to search across all triples
    query = f"""
    PREFIX owl: <http://www.w3.org/2002/07/owl#>
    PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
    PREFIX dwc: <http://rs.tdwg.org/dwc/terms/>
    PREFIX dwciri: <http://rs.tdwg.org/dwc/iri/>
    PREFIX dsw: <http://purl.org/dsw/>
    PREFIX dcterms: <http://purl.org/dc/terms/>
    PREFIX bet: <http://www.semanticweb.org/SirikitJoshi/BioEcoThai/>

    SELECT ?s ?p ?o
    WHERE {{
        ?s ?p ?o .
        FILTER (CONTAINS(LCASE(STR(?o)), LCASE("{term}")) || 
                CONTAINS(LCASE(STR(?p)), LCASE("{term}")) ||
                CONTAINS(LCASE(STR(?s)), LCASE("{term}")))
    }}
    LIMIT 10
    """
    sparql.setQuery(query)
    sparql.setReturnFormat(JSON)
    results = sparql.query().convert()
    
    # Format the results to include subject, predicate, and object
    formatted_results = [
        {
            "subject": result["s"]["value"] if "s" in result else None,
            "predicate": result["p"]["value"] if "p" in result else None,
            "object": result["o"]["value"] if "o" in result else None
        }
        for result in results["results"]["bindings"]
    ]

    return jsonify({"results": formatted_results})

@app.route('/sparql', methods=['POST'])
def run_sparql():
    sparql_query = request.data.decode('utf-8')
    if not sparql_query:
        return jsonify({"head": {"vars": []}, "results": {"bindings": []}})

    sparql = SPARQLWrapper(SPARQL_ENDPOINT)
    sparql.setQuery(sparql_query)
    sparql.setReturnFormat(JSON)

    try:
        results = sparql.query().convert()

        # Reformat results to include "head" and "bindings" as expected by the front end
        formatted_results = {
            "head": results.get("head", {}),
            "results": {
                "bindings": [
                    {key: {"type": value.get("type", ""), "value": value.get("value", "")} 
                     for key, value in result.items()}
                    for result in results.get("results", {}).get("bindings", [])
                ]
            }
        }
        return jsonify(formatted_results), 200

    except Exception as e:
        print("Error:", str(e))
        return jsonify({"error": f"Failed to fetch SPARQL results. Please check your query or the server. Error: {e}"}), 500

if __name__ == "__main__":
    app.run(debug=True)
