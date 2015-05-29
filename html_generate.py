# A python script to generate html from text

EXAMPLE_TEXT = """TITLE: Why Computers are Stupid
DESCRIPTION: The phrase "computers are stupid" refers 
to how they interpret instructions literally. This 
means that small typos can cause big problems.
TITLE: Python
DESCRIPTION: Python is a "programming language." It 
provides programmers a way to write instructions for a 
computer to execute in a way that the computer can understand.
TITLE: While Loops
DESCRIPTION: A while loop repeatedly executes the body of 
the loop until the "test condition" is no longer true."""

def generate_concept_HTML(concept_title, concept_description):
	html_text_1 = ''' 
<div class="concept">	
	<div class="concept-title">	
		''' + concept_title
	html_text_2 = ''' 
	</div> 
	<div class="concept-description"> 
		''' + concept_description
	html_text_3 = ''' 
	</div>
</div>'''
	full_html_text = html_text_1 + html_text_2 + html_text_3
	return full_html_text
	
def get_concept_by_position(text, start_location):
    concept_start = text.find('TITLE:',start_location)
    concept_end = text.find('TITLE:',start_location+7)
    if concept_end != -1:
        concept = text[concept_start:concept_end]
    else:
        concept = text[concept_start:]
    return concept
	
def get_title(concept):
    start_location = concept.find('TITLE:')
    end_location = concept.find('DESCRIPTION:')
    title = concept[start_location+7 : end_location-1]
    return title

def get_description(concept):
    start_location = concept.find('DESCRIPTION:')
    description = concept[start_location+13 :]
    return description	
	
def generate_all_html(text):
	concept_start = text.find('TITLE:')
	html = ' '
	while concept_start != -1:
		concept = get_concept_by_position (text,concept_start)
		title = get_title(concept)
		description = get_description(concept)
		html = html + generate_concept_HTML(title, description)
		concept_start = text.find('TITLE:',concept_start+1)
	return html	
		
	
print generate_all_html(EXAMPLE_TEXT)