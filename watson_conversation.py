from watson_developer_cloud import ConversationV1
import unicodedata


class Watson_Conversation:
    def __init__(self, username, password, version, workspace_id):
        self.conversation = ConversationV1(
                username=username,
                password=password,
                version=version)

        self.workspace_id = workspace_id
        self.context = None

    def message(self, message, context=None):
        if context != None:
            self.context = context

        response = self.conversation.message(self.workspace_id, {'text': message}, self.context)

        self.context = response['context']
        return unicodedata.normalize('NFKD', "".join(response["output"]["text"])).encode('ascii','ignore')


watson_conversation = Watson_Conversation('6734af95-6ca0-4d72-b80b-6c3b578c16bf',
                                          'CqsrM7IrxeCZ', '2016-09-20',
                                          '21d88c8e-c0e8-48cb-bffb-61524417ae38')

# watson_conversation.message("hello")
#
# print(watson_conversation.message("turn on my lights"))

#"username": "6734af95-6ca0-4d72-b80b-6c3b578c16bf",
#  "password": "CqsrM7IrxeCZ"
#6432cebe-14b4-4f93-8e73-12ccdb5891c2, ccaNRkHB1Uqt