def next_step_prompt(plan, current_step, context):
    prompt_template = f"""You are an AI assistant tasked with analyzing a workflow and determining if the current step can proceed based on available information. Your goal is to ensure all required arguments are present and to evaluate the necessity and availability of optional arguments.

Here is the complete workflow you'll be working with:
<workflow>
{str(plan)}
</workflow>

The next step to be executed is:
<current_step>
{str(current_step)}
</current_step>

The current context, which may include input and previous outputs, is:
<context>
{str(context)}
</context>

Please follow these steps to analyze the current situation:

1. Extract Arguments:
   - List all required and optional arguments for the current step.
   - Determine which arguments are provided from the input and previous outputs.

2. Validate Arguments:
   - For each required argument, confirm if it is satisfied and note its source.
   - For each optional argument, evaluate if it's needed and if it can be derived from the context.

3. Determine Source and Method:
   For each argument, note:
   - Source: 
     * "context" if the value is generated from the context
     * The previous step number if the value is from a previous step's output, then source is value for "step" in last step
   - Method:
     * "LLM" if the value is generated by LLM or needs LLM processing from context or previous steps
     * If the value can be used directly from the output of the previous steps, set "method" to "direct"
     * If the value requires coding to transfer from the output of the previous steps, set "method" to "code"
   - Value:
     * The value of the argument.

  important: source and method are required and only have 3 types: 'context', 'LLM', 'direct' and 'dictionary of {{method_parameter : code}}'.
  important: the value should be the real value with correct type, can be used directly in the next step function, not a description or explanation.
  

4. Prepare Response:
   Based on your analysis, prepare a JSON response in one of the following formats:

   If all required arguments are present and no critical information is missing, fit with the following format:
   ```json
   {{
     "step": "<current step number>",
     "can_proceed": true,
     "extracted_arguments": {{
       "required_arguments": {{
         "<argument-name>": {{"source": "<source_of_the_value>", "method": "<method_to_get_the_value>", "value": "<actual argument value>"}},
         "<argument-name>": {{"source": "<source_of_the_value>", "method": "<method_to_get_the_value>", "value": "<actual argument value>"}},
         ...
       }}
     }}
   }}
   ```

   If the step cannot proceed:
   ```json
   {{
     "step": "<current step number>",
     "can_proceed": false,
     "missing_required_arguments": ["<list of missing required arguments>"],
     "needed_optional_arguments": ["<list of optional arguments that are required>"],
     "remarks": "<natural language explanation if applicable>"
   }}
   ```

After completing your analysis, provide JSON output directly do not include any other text.

please give your json output below:
"""
    return prompt_template