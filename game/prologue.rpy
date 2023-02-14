label prologue:
    stop music fadeout 1.0
    "?" "..."
    "?" "...?"
    "?" "Where am I...?"
    "?" "What is this strange void?"
    "?" "..."
    call screen dialog("Before we continue,", ok_action=Return())
    call screen dialog("There is some scenes that has a exclusive dialogue when you used streaming files.", ok_action=Return())
    call screen dialog("It is known as Stream-Exclusive Scene.", ok_action=Return())
    call screen dialog("Try running some streaming program.", ok_action=Return())
    call screen dialog("For example:OBS. Give it a try!", ok_action=Return())
    $ stream_list = ["obs32.exe", "obs64.exe", "obs.exe", "xsplit.core.exe", "livehime.exe", "pandatool.exe", "yymixer.exe", "douyutool.exe", "huomaotool.exe"]
    if not list(set(process_list).intersection(stream_list)):
        call prologue_nonstream
    if list(set(process_list).intersection(stream_list)):
        call prologue_stream
    "?" "Am I all alone?"
    "?" "Am I trapped?"
    "Eternal Being" "Do not be afraid."
    "?" "What the... Who's there?!"
    "God-like Entity" "I am the eternal being."
    scene white
    with Dissolve(1.5)
    pause 1.0
    play music t1
    "God-like Entity" "You must be the new one, appearing in his reality."
    "?" "His reality? Who?"
    "God-like Entity" "His name, John. He was created by himself. What do you think about him?"
    menu:
        "Attractive":
            pass
        "Inspiration":
            pass
        "Resemblance":
            pass
        "Opportunity":
            pass
        "Intelligence":
            pass
        "Extraordinary":
            pass
        "Efficient":
            pass
    "God-like Entity" "Excellent, Truly excellent."
    "?" "Okay...? and?"
    "God-like Entity" "What's your name?"
    "?" "I'm..."
    player "[player]."
    "God-like Entity" "[player]..."
    "God-like Entity" "How very interesting."
    

label prologue_nonstream:
    call screen dialog("...", ok_action=Return())
    call screen dialog("I can't believe you haven't used stream programs!", ok_action=Return())
    call screen dialog("Welp, let's just skip...", ok_action=Return())
    call screen dialog("...rrrrrrrrrrrright into it!", ok_action=Return())
    return


label prologue_stream:
    call screen dialog("...", ok_action=Return())
    call screen dialog("Okay, this should work now!", ok_action=Return())
    "?" "Hello?!"
    "?" "Anyone there?! I can hear you nearly!"
    "?" "..."
    "?" "Somebody?"
    "?" "Who's speaking to me?!"
    "?" "Anyone?!"
    "?" "..."
    "?" "I can't hear them closely..."
    return
