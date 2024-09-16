# Helper function for cleaner printing
def print_output(output):
    import textwrap
    print(textwrap.fill(str(output),width= 120))

# Show available models
# def get_models():
#     for model in genai.list_models():
#         print(model.name)