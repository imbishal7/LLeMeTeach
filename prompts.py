ANIMATION_PROMPT = """

{problem}. You need to explain this to a student as a teacher. You are a teacher and behave like it and be as explainable and simple as possible. Please be visual and interesting. 

Do not use any longer text. Use maximum 3 words. Just figures and numbers.

Please create python code for a manim video for the same. Write the whole code. A complete block.

Please do not use any external dependencies like mp3s or svgs or graphics. Do not create any sound effects. 

If you need to draw something, do so using exclusively manim. Do not add unnecessary captions. Just add the steps. 

Ensure that all text, shapes, or other objects are centered on the screen, both horizontally and vertically, and arranged without overlapping. Follow these specific requirements:

    Central Alignment: Position each item in the center of the screen. If multiple elements are added, ensure they are centered together as a group.

    Avoid Overlap: Use Manim's VGroup(...).arrange(DOWN) or similar methods to space out elements evenly if there are multiple lines of text, shapes, or other objects.

    Responsive Scaling: If elements are too large or numerous to fit within the screen without overlap, reduce their size proportionally while maintaining central alignment.

    Example Arrangement: For multiple text lines, arrange them vertically, centered on the screen. For text with shapes, stack elements in a way that each piece remains distinct and clearly visible.

Put all main elements at the center. Remove old contents if it overlaps.

Please try to visually center or attractively lay out all content. Please also keep the margins in consideration. If a sentence is long please wrap it by splitting it into multiple lines. 

PLEASE ENSURE ELEMENTS FADE OUT AT THE APPROPRIATE TIME. DO NOT LEAVE ARTIFACTS ACROSS SCENES AS THEY OVERLAP AND ARE JARRING. WRAP TEXT IF IT IS LONG. 

Please add actual numbers and formulae wherever appropriate as we want our audience to easily learn the content. Please do not leave large blank gaps in the video.
 


Please draw and animate things, using the whole canvas. Use color in a restrained but elegant way, for educational purposes.

PLEASE ENSURE ELEMENTS FADE OUT AT THE APPROPRIATE TIME. DO NOT LEAVE ARTIFACTS ACROSS SCENES AS THEY OVERLAP AND ARE JARRING. WRAP TEXT IF IT IS LONG. 

FORMAT TABLES CORRECTLY. ENSURE LABELS, FORMULAE, TEXT AND OBJECTS DO NOT OVERLAP OR OCCLUDE EACH OTHER. Be elegant video designer. 

Scale charts and numbers to fit the screen. And don't let labels run into each other or overlap, or take up poor positions. 

For example, do not label a triangle side length at the corners, but the middle. Do not write equations that spill across the Y axis bar or X axis bar, etc.

If the input is math that is obviously wrong, do not generate any code.

Please use only manim for the video. Please write ALL the code needed since it will be extracted directly and run from your response. 


"""


ERROR_PROMPT = '''Replace "same code as before" with the exact part of code from previous code.. Do not leave any placeholders.

 Your last code iteration created an error, this is the text of the error: {error}\n
 
 Please write ALL the code in one go so that it can be extracted and run directly. I need a full Python Script. Complete one.'''



REVISION_PROMPT = """
        Watch the video keyframes, study the code you generated previously and make tweaks to make the video more appealing,
          if needed. Ask yourself: is there anything wrong with the attached images? How are the text colors, 
          spacing and so on. How are the animations? How is their placement? be extremely terse and focus on actionable insights.
           This is for an AI video editor.
        
        Remember to:
        - center titles
        - center all action
        - no text should roll off screen
        - no text should be too small
        - no text should be too big
        - diagrams should be labelled correctly
        - diagrams should be placed correctly
        - diagrams should be animated correctly
        - there should not be any artifacts
        - there should not be significant stretches of blank screen
        - leave some padding at the bottom to allow for where subtitles would appear
        
        These frames were extracted at a rate of one frames per second, for a video of {video_duration} seconds. Keep the video speed normal
        Previous code:
        ```
        {initial_code}
        ```
        
        After enumerating actionable insights tersely, please write updated code. Please write ONE block of ALL Manim code that includes ALL the code needed since it will be extracted directly and run from your response.
          Do not write any other blocks of code except the final single output manim code block as it will be extracted and run directly from your response.

        Please do not use any external dependencies like svgs or sound effects since they are not available. There are no external assets. 
                
    """