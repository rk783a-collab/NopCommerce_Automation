class PostData:
    @staticmethod
    def create_post(
            title = "Playwright Automation",
            body = "API testing with python and pytest",
            userId = 1
    ):
        return {
            "title": title,
            "body": body,
            "userId": userId
        }