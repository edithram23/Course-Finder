# Course Finder Project

This project aims to develop a comprehensive course finder tool that suggests the most relevant courses based on user preferences. It integrates multiple approaches to enhance the search and recommendation process, including FAISS, Gemini LLM with text-only output, and Gemini LLM with both text and link output.

## Project Components

### **Course Data Scraper**

The `scrapper.py` script collects data such as course titles, descriptions, instructors, and URLs from AnalyticsVidhya. 
- **File**: `scrapper.py`
  
### 1. **FAISS-Based Course Finder**

The FAISS (Facebook AI Similarity Search) implementation provides a fast and efficient way to find the most relevant courses based on user preferences.
Embeddings were generated using a HF Sentence Transformer - all-MiniLM-L6-v2

- **Files**: `Faiss_app.py`, `course_data.csv`, `requirements.txt`
- **Approach**: Uses FAISS to create a similarity search index of courses, allowing for real-time course recommendations.

### 2. **Gemini LLM - Text-Only Output**

This version of the Gemini LLM-based course finder provides course recommendations in text format only.

- **Files**: `gemini_app.py`, `database.txt`, `requirements.txt`
- **Approach**: Uses a language model to interpret user input and suggest relevant courses based on textual information.

### 3. **Gemini LLM - Text & Link Output**

This implementation of the Gemini LLM-based course finder provides both text and link output for each course, allowing users to directly access the suggested courses.

- **Files**: `gemini_link_app.py`, `data_base.txt`, `requirements.txt`
- **Approach**: Enhances the Gemini LLM model to provide detailed course information, including links for easier access.

## How to Run the Project

1. **Scrape Course Data**
   - Run the scraper to collect course information:
     ```
     python scrapper.py
     ```
   - Ensure that the required dependencies are installed from `requirements.txt` in the scraper folder.

2. **Run the Course Finder Tool**
   - Choose one of the three approaches:
     - **FAISS-Based Search**:
       ```
       python Faiss_app.py
       ```
     - **Gemini LLM (Text-Only)**:
       ```
       python gemini_app.py
       ```
     - **Gemini LLM (Text & Link Output)**:
       ```
       python gemini_link_app.py
       ```
   - Install dependencies using the corresponding `requirements.txt` file.

## Summary of Approaches

1. **FAISS-Based Course Finder**: Uses similarity search to efficiently recommend courses based on a pre-indexed dataset.
2. **Gemini LLM (Text-Only)**: Utilizes a language model to provide course recommendations in a simple text format.
3. **Gemini LLM (Text & Link Output)**: Extends the text-based approach by including course links for direct access, providing a richer user experience.

## Choosing the Right Approach

For this task, using similarity search with FAISS is more than sufficient to achieve effective course recommendations. FAISS provides a fast and efficient way to index and search for similar courses based on user preferences, making it a practical solution for this type of project. 
