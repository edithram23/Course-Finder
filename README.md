# Course Finder Project

This project aims to develop a comprehensive course finder tool that helps users find the most relevant courses on Analytics Vidhya's platform based on user preferences. The project involves three different approaches for enhancing the search and recommendation process, including FAISS, Gemini LLM with text-only output, and Gemini LLM with both text and link output. Additionally, a data scraper is used to gather course information from Analytics Vidhya’s platform.

## Project Components

### **Course Data Scraper**

The `scrapper.py` script collects data such as course titles, descriptions, instructors, and URLs from AnalyticsVidhya. 
- **File**: `scrapper.py`
  
### 1. **FAISS-Based Course Finder**

The FAISS (Facebook AI Similarity Search) implementation provides a fast and efficient way to find the most relevant courses based on user preferences.
Embeddings were generated using a HF Sentence Transformer - all-MiniLM-L6-v2
- **Approach**: Uses FAISS to create a similarity search index of courses, allowing for real-time course recommendations.

### 2. **Gemini LLM - Text-Only Output**

This version of the Gemini LLM-based course finder provides course recommendations in text format only.
- **Approach**: Uses a language model to interpret user input and suggest relevant courses based on descriptions.

### 3. **Gemini LLM - Text & Link Output**

This implementation of the Gemini LLM-based course finder provides both text and link output for each course, allowing users to directly access the suggested courses.
- **Approach**: Enhances the Gemini LLM model to provide detailed course information, including links for easier access.

## How to Run the Project

**Access links**
   **Deployed in HF SPACES**
   - Choose one of the three approaches:
     - **FAISS-Based Search**:
       
       ```
          https://huggingface.co/spaces/edithram23/analyticsvidhya
       ```
     - **Gemini LLM (Text-Only)**:
       ```
       https://huggingface.co/spaces/edithram23/analyticsvidhya-gemini
       ```
     - **Gemini LLM (Text & Link Output)**:
       ```
       https://huggingface.co/spaces/edithram23/analyticsvidhya-gemini-link
       ```


## Choosing the Right Approach

For this task, using similarity search with FAISS is more than sufficient to achieve effective course recommendations. FAISS provides a fast and efficient way to index and search for similar courses based on user preferences, making it a practical solution for this type of project. 
