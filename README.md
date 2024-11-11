# BioEcoThai

## Overview
The **BioEcoThai** Ontology Project is a comprehensive ontology that integrates biodiversity and ecotourism data specific to Thailand. The aim is to support sustainable biodiversity conservation and ecotourism by creating a unified knowledge graph that promotes responsible tourism, facilitates research, and aids conservation efforts. The ontology draws from existing standards such as the DarwinCore terms and Darwin-Semantic Web (DSW) ensuring alignment with global biodiversity initiatives like the Global Biodiversity Information Facility (GBIF).

## Goals
- **Promote Sustainable Tourism**: Support responsible tourism by linking biodiversity hotspots with ecotourism opportunities, allowing tourists and researchers to identify areas of high conservation value and cultural importance.
- **Aid Researchers and Policymakers**: Provide a knowledge base that helps researchers and policymakers in making informed decisions about biodiversity conservation.
- **Facilitate Data Integration**: Enable seamless integration of various biodiversity and ecotourism datasets to create a comprehensive understanding of Thailand's natural resources.

## Features
- **Standardized DarwinCore Terms**: The ontology adopts standardized DarwinCore terms, widely recognized and used within the biodiversity community, to promote consistency and facilitate data exchange.
- **Alignment with GBIF**: The ontology structure and terminology are aligned with GBIF to ensure global interoperability and open access to biodiversity data.
- **Ecotourism Data**: Incorporates ecotourism-related concepts to link biodiversity conservation efforts with tourism activities, supporting sustainable development initiatives.
- **High Conservation Value Analysis (HCVA)**: Incorporates High Conservation Value (HCV) analysis, classifying areas based on species richness, endangerment levels, and cultural significance to guide conservation and tourism.

## Structure
The BioEcoThai ontology consists of two main components:
1. **Biodiversity Component**: Includes taxonomic classifications, species attributes, habitats, and conservation statuses. This component is aligned with biodiversity ontologies such as DSW, and utilizes DarwinCore terms and GBIF relations.
2. **Ecotourism Component**: Covers tourism sites, cultural and natural heritage, and their connections to biodiversity. The ontology aims to support responsible tourism by highlighting areas of ecological and cultural importance.

## Use Cases
- **Researchers and Conservationists**: The ontology can be used by researchers to study biodiversity patterns, conservation needs, and species distribution, facilitating data-driven conservation decisions.
- **Ecotourists**: Tourists can use the knowledge graph to find ecotourism sites with high biodiversity and cultural value, encouraging responsible tourism.
- **Policy Makers**: The integrated data can help policymakers identify areas needing protection and create sustainable tourism strategies aligned with biodiversity conservation.

## Getting Started
To get started with the BioEcoThai Ontology Project:
1. Clone the repository:
   ```bash
   git clone https://github.com/scarredwitch/BioEcoThai.git
   ```
2. Load the ontology into a tool like Protégé to explore and make contributions.

## Running the Frontend with Apache Jena Fuseki
To set up a local instance of the BioEcoThai frontend using Apache Jena Fuseki, follow these steps:

1. **Install Apache Jena Fuseki**: Download and install Apache Jena Fuseki from [https://jena.apache.org/download/](https://jena.apache.org/download/).

2. **Start Apache Jena Fuseki**:
   - Navigate to the folder where you installed Fuseki.
   - Start the Fuseki server by running the following command:
     ```bash
     ./fuseki-server
     ```
   - Access the Fuseki server at [http://localhost:3030/](http://localhost:3030/) to manage datasets.

3. **Load the Ontology**:
   - Create a new dataset in Fuseki and upload the BioEcoThai ontology file (e.g., `BioEcoThai.rdf`). This will allow you to query the ontology using SPARQL.

4. **Run the Frontend** (Python Flask API):
   - Ensure that the Fuseki server is running.
   - Navigate to the `frontend` folder in the cloned repository:
     ```bash
     cd BioEcoThai/frontend
     ```
   - Open your terminal (e.g., VS Code terminal) and run the following command to start the Python application:
     ```bash
     python app.py
     ```
   - The frontend should now be accessible at [http://localhost:5000/](http://localhost:5000/).

5. **Connecting Frontend to Fuseki**:
   - Make sure to point to your local Fuseki instance at `http://localhost:3030/ds/query`.
   - This will allow the frontend to interact with the SPARQL endpoint and display data from the BioEcoThai ontology.


## Contributing
Contributions are welcome! If you'd like to contribute to the project, please fork the repository and create a pull request. Feel free to report any issues or suggest improvements.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Acknowledgments
- **GBIF**: For providing open access to biodiversity data and supporting standardization efforts.
- **DarwinCore**: For standardized terms that facilitate data sharing and consistency in the biodiversity domain.

## Contact
For more information or questions, feel free to contact the project maintainers via GitHub or at sirikitjoshi@gmail.com.

