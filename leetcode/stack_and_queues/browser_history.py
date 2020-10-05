# link:https://leetcode.com/problems/design-browser-history/

class BrowserHistory:

    def __init__(self, homepage: str):
        self.forw_memo = []     # forw_memo stores the future url
        self.back_memo = []     # back_memo stores the previous url
        self.curr_url = homepage

    def visit(self, url: str) -> None:
        self.back_memo.append(self.curr_url)
        self.curr_url = url
        self.forw_memo = []      # clear forw_memo
        
    def back(self, steps: int) -> str:
        while self.back_memo and steps >= 1:
            self.forw_memo.append(self.curr_url)
            pop_url = self.back_memo.pop()
            self.curr_url = pop_url
            steps -= 1
        
        return self.curr_url

    def forward(self, steps: int) -> str:
        while self.forw_memo and steps >= 1:
            self.back_memo.append(self.curr_url)
            pop_url = self.forw_memo.pop()
            self.curr_url = pop_url
            steps -= 1
            
        return self.curr_url


