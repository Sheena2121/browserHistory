class BrowserHistory:
    def __init__(self):
        self.map = {}
        self.curr_index = -1
        self.map[self.curr_index] = ""

    def current_page(self):
        return self.map[self.curr_index]

    def go_to(self, page):
        self.curr_index += 1
        print("the new curr_index is {}".format(self.curr_index))
        self.map[self.curr_index] = page
        for key, value in self.map.items():
            if key > self.curr_index:
                del self.map[key]

    def go_back(self):
        self.skip_backward(1)

    def go_forward(self):
        self.skip_forward(1)

    def skip_backward(self, N):
        if self.curr_index - N in self.map.keys():
            self.map.get(self.curr_index - N)
            self.curr_index = self.curr_index - N
        else:
            print("tried to go back too far!")
        self.current_page()
        print("the new curr_index is {}".format(self.curr_index))

    def skip_forward(self, N):
        if self.curr_index + N in self.map.keys():
            self.map.get(self.curr_index + N)
            self.curr_index = self.curr_index + N
        else:
            print("tried to go forward too far!")
        self.current_page()
        print("the new curr_index is {}".format(self.curr_index))


browserHistory = BrowserHistory()

browserHistory.go_to("NYT")
print(browserHistory.current_page())

browserHistory.go_to("google")
print(browserHistory.current_page())

browserHistory.go_to("amazon")
print(browserHistory.current_page())

browserHistory.go_to("FB")
print(browserHistory.current_page())

browserHistory.skip_backward(2)

print(browserHistory.current_page())

browserHistory.skip_backward(3)

print(browserHistory.current_page())

browserHistory.skip_forward(2)

print(browserHistory.current_page())
