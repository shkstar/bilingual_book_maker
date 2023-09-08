from litellm import completion
from book_maker.cli import main

if __name__ == "__main__":
    
  # Initialize translator
  translate_model = completion

  # Call completion with Claude  
  response = completion(model="claude-2", messages=messages)

  main(model="claude")
