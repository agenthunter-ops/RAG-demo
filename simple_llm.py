# Import the necessary packages
from langchain_google_genai import ChatGoogleGenerativeAI
import os

# Set your Google Gemini API key
os.environ["GOOGLE_API_KEY"] = "AIzaSyD9DtgmNZFq9BK1R48I54xzF6ftvuIfOBU"

# Initialize the Gemini model
chat_model = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",  # Updated to current available model
    temperature=0.7,
    max_output_tokens=256
)

# Get the query from the user input
query = input("Please enter your query: ")

# Get the response from the model
response = chat_model.invoke(query)

# Print the response
print(response.content)


