import time
def scroller(page):
    end = page.evaluate("document.body.scrollHeight")
    while True:
        # jump to that end
        page.mouse.wheel(0, int(end))
        time.sleep(2)
        newend = page.evaluate("document.body.scrollHeight")
        print(end, newend)
        if end == newend:
            print("We are done")
            break
        else:
            end = newend