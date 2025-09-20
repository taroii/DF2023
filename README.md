# Attorney Search - ASA DataFest 2023 

A proof-of-concept tool designed to improve the classification and routing of legal questions on the American Bar Association's Free Legal Answers platform.

**🚀 [Live Demo on Replit](https://replit.com/@taroii/DF2023-Attorney-Search?v=1)**

**📄 [Project Details](https://taroiyadomi.netlify.app/articles/attorney_search/)**

**📊 [Presentation Slides](https://docs.google.com/presentation/d/1bQCYkxnFNVQGjQCFuIDbAG_xSq_VcFGqViplO63UB44/edit?usp=sharing)**

*ACM DataFest 2023 - Team DataMinerz*

## Overview

Attorney Search combines modern natural language processing (NLP) with demographic-aware scoring to automatically classify legal questions and match them with the most suitable attorneys. This addresses critical gaps in the current Free Legal Answers platform.

### The Problem

The American Bar Association's Free Legal Answers platform faces several structural issues:

1. **Manual Categorization by Clients**: Clients must select legal categories themselves, often leading to inaccurate classification due to language barriers or unfamiliarity with legal terms.

2. **Fragmented Subcategories**: Over 340 subcategories exist across different U.S. states, many duplicative or semantically overlapping, causing inefficiency and errors.

3. **No Intelligent Routing**: Questions are answered by the first available lawyer regardless of their expertise, reducing response quality.

### The Solution

Attorney Search provides:
- **Automatic classification** using fine-tuned DistilBERT models
- **Simplified subcategories** through unsupervised clustering (340+ → 8 meaningful clusters)
- **Intelligent attorney matching** based on legal topic and client demographics

## System Architecture

### 1. Preprocessing
- Text standardization using lemmatization
- Removal of stopwords and punctuation

### 2. Classification
- Fine-tuned DistilBERT model predicts category and subcategory
- BERT-based embeddings for semantic understanding

### 3. Subcategory Simplification
- K-Means clustering reduces 340+ subcategories into 8 clusters
- Maintains semantic meaning while improving efficiency

### 4. Matching and Scoring
- Combines legal classification with demographic data
- Scoring algorithm ranks attorneys by suitability
- Considers ethnicity, gender, and imprisonment status for personalized matching

## Getting Started

### Prerequisites
- Python 3.8+
- Flask
- Hugging Face Transformers
- python-dotenv

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/taroii/DF2023.git
   cd DF2023
   ```

2. **Install dependencies**
   ```bash
   pip install flask transformers torch python-dotenv requests pandas numpy
   ```

3. **Set up environment variables**

   Create a `.env` file in the root directory:
   ```bash
   HUGGINGFACE_API_TOKEN=your_huggingface_token_here
   ```

   Get your Hugging Face token from [https://huggingface.co/settings/tokens](https://huggingface.co/settings/tokens)

4. **Run the application**
   ```bash
   python main.py
   ```

5. **Open your browser**

   Navigate to `http://localhost:5000` to use the application.

## Usage

1. **Input Legal Question**: Enter your legal question in plain language
2. **Provide Demographics**: Fill in relevant demographic information
3. **Get Results**: Receive:
   - Predicted legal category and subcategory
   - List of three recommended attorneys ranked by compatibility

## Key Features

- **Automated Classification**: No need for clients to understand legal categories
- **Demographic-Aware Matching**: Considers client background for better attorney pairing
- **Simplified Categories**: Reduces complexity from 340+ to 8 meaningful clusters
- **Real-time Processing**: Instant classification and matching

## Technical Implementation

### Models Used
- **Category Classification**: `taroii/datafest_category`
- **Subcategory Classification**: `taroii/datafest_subcategory`
- Both models are fine-tuned DistilBERT variants hosted on Hugging Face

### Files Structure
```
├── main.py              # Flask application
├── model.py             # ML model integration
├── utils.py             # Utility functions
├── templates/           # HTML templates
├── static/             # CSS, JS, and assets
└── .env                # Environment variables (not in repo)
```

## Future Improvements

### Planned Enhancements
1. **Learned Scoring Models**: Replace hand-crafted weights with trainable neural networks
2. **Feedback Loop**: Add rating system to gather match quality data
3. **Expanded Features**: Include attorney specialties, languages, and performance metrics

### Research Directions
- Geographic and temporal pattern analysis
- Advanced demographic matching algorithms
- Multi-language support for broader accessibility

## Results and Impact

Attorney Search demonstrates measurable improvements in:
- **Classification Accuracy**: Automated categorization reduces client errors
- **Attorney Matching**: Demographic-aware scoring improves client satisfaction
- **System Efficiency**: Simplified categories reduce administrative overhead

## Contributing

This project was developed for ACM DataFest 2023. While the competition phase is complete, the codebase serves as a foundation for continued research in legal technology and access to justice.

## License

This project was created for ACM DataFest 2023 and is intended for educational and research purposes.

## Acknowledgments

- **Team DataMinerz** - ACM DataFest 2023 participants
- **American Bar Association** - For providing the Free Legal Answers platform data
- **Hugging Face** - For model hosting and inference API
- **ACM DataFest** - For the opportunity to work on meaningful real-world problems
