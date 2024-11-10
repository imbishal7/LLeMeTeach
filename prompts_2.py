ANIMATION_PROMPT = '''

Can you explain {problem} to a students. Please be visual and interesting. Consider using a meme if the audience is younger.

Please create python code for a manim video for the same. 

Please do not use any external dependencies like mp3s or svgs or graphics. Do not create any sound effects. 

If you need to draw something, do so using exclusively manim. Always add a title and an outro. Narrate the title and outro.

Please try to visually center or attractively lay out all content. Please also keep the margins in consideration. If a sentence is long please wrap it by splitting it into multiple lines. 

Please add actual numbers and formulae wherever appropriate as we want our audience   to learn math.

Do use voiceovers to narrate the video. The following is an example of how to do that:



Please do not use any external dependencies like svgs or mp3s or grpahics since they are not available. Draw with shapes and use colored letters, but keep it simple. There are no external assets. Constraints are liberating. 

First write the script explicitly and refine the contents and then write the code.

Please draw and animate things, using the whole canvas. Use color in a restrained but elegant way, for educational purposes.

Please add actual numbers and formulae wherever appropriate as we want our audience  to learn math. Please do not leave large blank gaps in the video. Make it visual and interesting. PLEASE ENSURE ELEMENTS FADE OUT AT THE APPROPRIATE TIME. DO NOT LEAVE ARTIFACTS ACROSS SCENES AS THEY OVERLAP AND ARE JARRING. WRAP TEXT IF IT IS LONG. FORMAT TABLES CORRECTLY. ENSURE LABELS, FORMULAE, TEXT AND OBJECTS DO NOT OVERLAP OR OCCLUDE EACH OTHER. Be elegant video designer. Scale charts and numbers to fit the screen. And don't let labels run into each other or overlap, or take up poor positions. For example, do not label a triangle side length at the corners, but the middle. Do not write equations that spill across the Y axis bar or X axis bar, etc.

If the input is math that is obviously wrong, do not generate any code.

Please use only manim for the video. Please write ALL the code needed since it will be extracted directly and run from your response. 

Take a deep breath and consider all the requirements carefully, then write the code.'''


ERROR_PROMPT = '''Your last code iteration created an error, this is the text of the error: {error}\nPlease write ALL the code in one go so that it can be extracted and run directly'''



REVISION_PROMPT = """
        Watch the video keyframes, study the code you generated previously and make tweaks to make the video more appealing, if needed. Ask yourself: is there anything wrong with the attached images? How are the text colors, spacing and so on. How are the animations? How is their placement? be extremely terse and focus on actionable insights. This is for an AI video editor.
        
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
        
        These frames were extracted at a rate of 1 frames per second, for a video of {video_duration} seconds. Keep the video speed 1.15x.
        
        Previous code:
        ```
        {initial_code}
        ```
        
        After enumerating actionable insights tersely, please write updated code. Please write ONE block of ALL Manim code that includes ALL the code needed since it will be extracted directly and run from your response. Do not write any other blocks of code except the final single output manim code block as it will be extracted and run directly from your response.

        Please do not use any external dependencies like svgs or sound effects since they are not available. There are no external assets. 
                
        Remember, your goal is to explain the concept easily. Please stick to explaining the right thing in an interesting way appropriate to the audience. The goal is to make a production grade math explainer video that will help viewers quickly and thoroughly learn the concept. You are a great AI video editor and educator. Keep the video speed 1.15x. Thank you so much! Take a deep breath and get it right!
    """