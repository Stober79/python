experience = 2
languages = ["python", "javaScript", "typescript", "java"]
contractType = "b2b"
if experience>= 2 and "python" in languages and "java" in  languages:
    if contractType == "b2b" or contractType == "employement":
        print("you are a good candidate for this job")
    else:        print("you are not a good candidate for this job")
else:    print("you are not a good candidate for this job")