"""
PostOffice from week 7, with read_inbox and search_inbox.

Changes to the original class: messages now have a title (optional,
so old calls still work) and a 'read' flag, both used by the new methods.
"""


class PostOffice:
    """A post office that lets users send, read and search messages."""

    def __init__(self, usernames):
        self.message_id = 0
        self.boxes = {user: [] for user in usernames}

    def send_message(self, sender, recipient, message_body, urgent=False, title=""):
        """
        Sends a message and returns its id.

        :param urgent: If True, puts the message at the top of the inbox.
        """
        user_box = self.boxes[recipient]
        self.message_id += 1
        message = {'id': self.message_id, 'title': title, 'body': message_body,
                   'sender': sender, 'read': False}
        if urgent:
            user_box.insert(0, message)
        else:
            user_box.append(message)
        return self.message_id

    def read_inbox(self, username, count=None):
        """
        Returns the first unread messages and marks them as read.

        :param count: How many messages to read. If None, reads all.
        """
        unread = [message for message in self.boxes[username] if not message['read']][:count]
        for message in unread:
            message['read'] = True
        return unread

    def search_inbox(self, username, text):
        """Returns all messages that contain text in their title or body."""
        return [message for message in self.boxes[username]
                if text in message['title'] or text in message['body']]


if __name__ == "__main__":
    post_office = PostOffice(['Newman', 'Mr. Peanutbutter'])
    post_office.send_message('Mr. Peanutbutter', 'Newman', 'Hello, Newman.', title='Hi')
    post_office.send_message('Mr. Peanutbutter', 'Newman', 'See you soon!', title='Party')
    print(post_office.search_inbox('Newman', 'Party'))
    print(post_office.read_inbox('Newman', 1))
    print(post_office.read_inbox('Newman'))
