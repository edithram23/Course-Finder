# Course Finder Project

This project aims to develop a comprehensive course finder tool that suggests the most relevant courses based on user preferences. It integrates multiple approaches to enhance the search and recommendation process, including FAISS, Gemini LLM with text-only output, and Gemini LLM with both text and link output. Additionally, a data scraper is provided to gather course information from various online sources.

## Project Components

### 1. **Course Data Scraper**

The `scrapper.py` script collects data such as course titles, descriptions, instructors, and URLs from various online platforms. This data serves as the foundation for the recommendation engines.

- **Files**: `scrapper.py`, `requirements.txt`
- **Purpose**: To gather relevant course information that can be used by the recommendation models.

### 2. **FAISS-Based Course Finder**

The FAISS (Facebook AI Similarity Search) implementation provides a fast and efficient way to find the most relevant courses based on user preferences.

- **Files**: `Faiss_app.py`, `course_data.csv`, `requirements.txt`
- **Approach**: Uses FAISS to create a similarity search index of courses, allowing for real-time course recommendations.

### 3. **Gemini LLM - Text-Only Output**

This version of the Gemini LLM-based course finder provides course recommendations in text format only.

- **Files**: `gemini_app.py`, `database.txt`, `requirements.txt`
- **Approach**: Uses a language model to interpret user input and suggest relevant courses based on textual information.

### 4. **Gemini LLM - Text & Link Output**

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

## Requirements

- Python 3.7+
- Dependencies specified in each component's `requirements.txt`

## Workflow

1. **Data Gathering**: Use the scraper to collect course information.
2. **Indexing/Model Setup**: Use FAISS or the Gemini LLM models to set up the course finder.
3. **User Interaction**: Users input their preferences, and the application suggests relevant courses based on the chosen method.
4. **Output**: Recommendations are displayed to the user, either in text format or with additional links, depending on the approach.

