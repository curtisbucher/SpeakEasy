"""A powerful, lightweight machine-learning Python chat engine."""

from json import dump, load, JSONDecodeError # JSON used for data persistence.

def learn(prompt, response, score=True):
    """Learn response as a reply to prompt.
    
    Parameters:
        prompt | str: A theoretical prompt that might be encountered.
        response | str: The response to be associated with prompt.
        score | bool / complex / float / int | default True: A value between 0 
            and 1 (inclusive) indicating the effectiveness of response as a 
            reply to prompt. If it is perfect, use 1 (or True). If it makes no 
            sense, use 0 (or False). Any value between these is also valid, for 
            more nuanced scoring. If the value is not in this range, the closest 
            valid value (0 or 1) is used. The imaginary parts of complex numbers 
            are not considered.
    """

    score = max(0, min(score.real, 1)) # 0 <= score <= 1.
    data = _load()

    # Add the phrases to the nested dict data, and assign them a list of two 
    # values: [cumulative_score, number_of_trials]. 
    
    # These values are used by _lapl in the reply function to infer the 
    # probability that response will be a valid reply to a future prompt.
    
    if prompt not in data:
        data[prompt] = {response: [score, 1]}
        
    elif response not in data[prompt]:
        data[prompt][response] = [score, 1]
        
    else:
        data[prompt][response][0] += score
        data[prompt][response][1] += 1

    _dump(data)

def reply(prompt):
    """Return a response to prompt.
    
    Parameters:
        prompt | str: A prompt to find a response for.
        
    Returns:
        response | str: The best known reply to prompt.
    """
    
    def _lapl(values): return (values[0] + 1) / (values[1] + 2) # Laplace's law.

    responses = {}
    data = _load()

    # Check every substring of prompt (with duplicates) against the prompts used 
    # in training. 
    
    # If a substring exists in this known prompt, add the prompt (and its values) 
    # to responses.

    for substring in _subs(prompt):
        for known_prompt in data:
            if substring not in known_prompt: continue
            for response in data[known_prompt]:
                if response not in responses:
                    responses[response] = data[known_prompt][response]
                else:
                    responses[response][0] += data[known_prompt][response][0]
                    responses[response][1] += data[known_prompt][response][1]
                
    # Using Bayesian inference from _llaw, transform responses into a dict of 
    # how successful each candidate response is expected to be as a reply to 
    # prompt, based on how successful they've been for each of its substrings.

    responses = {response: _lapl(responses[response]) for response in responses}
    
    # Return the response with the highest expected probability of success. 
    
    # Because the max function preserves the order of the responses and returns 
    # the first one, responses based on the longer substrings (which are more 
    # representative of the full prompt) are chosen in the event of a tie. 
    
    # _subs also includes the empty string '', which gurantees that every learned 
    # response has the opportunity to be chosen. In the event that no learned 
    # data exists, prompt is the default value returned.

    return max(responses, key=responses.get, default=prompt)

def _dump(data):
    """Merge persistent data with speakeasy_data.json."""
    
    file_data = _load()
    file_data.update(data)
    
    with open("speakeasy_data.json", 'w') as file:
        dump(file_data, file)

def _load():
    """Return persistent data from speakeasy_data.json."""
    
    try:
        
        with open("speakeasy_data.json") as file:
            return load(file) 
        
    except (FileNotFoundError, JSONDecodeError):
        return {} # Missing or corrupted file.

def _subs(string):
    """Return list of substrings for string (with duplicates), longest first."""

    subs = [''] # Empty string is present in all strings.
    
    for start in range(len(string)):
        for end in range(start+1, len(string)+1):
            subs.append(string[start:end])
            
    return sorted(subs, key=len, reverse=True)
