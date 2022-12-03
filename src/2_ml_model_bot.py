from common.classes.classes import ResponseException
from common.methods.getResearchPapers import getResearchPapers
from common.methods.parseUpdate import UpdateInfo
from common.methods.sendTelegramMessage import sendTelegramMessage
from common.methods.startServer import startServerPolling
from common.methods.summarizeWithML import summarizeWithML


def parseResponse(update_info: UpdateInfo):
    sender = update_info['sender']
    message = update_info['message']
    # use this keyword to search the papers
    keyword = message
    # send the messages to this chat
    chat_id = update_info['chat_id']
    print(f"User {sender} sent {keyword} on chat {chat_id}")

    abstracts_text = ""

    sendTelegramMessage(chat_id, "Elaborating request...")

    try:
        response = getResearchPapers(keyword)
        if len(response['results']) == 0:
            sendTelegramMessage(
                chat_id, 'CoreAC was not able to find any result for ' + keyword)
        else:
            for paper in response['results']:
                # TODO 1: Missing code here
    except Exception:
        return_msg = 'Error getting the research papers. Please retry later.'
        sendTelegramMessage(chat_id, return_msg)
        return

    # - summarize ------------------------------------------------------------------------------------------------------

    # Sends a message to the user informing him that the summarization could take time
    return_msg = f"Summarizing the paper Abstracts, this can take some time..."
    sendTelegramMessage(chat_id, return_msg)

    try:
        # TODO 2: call summarizeWithML() function to summarize the abstracts and send the result to the user

    except ResponseException as e:
        # Handles a Hugging Face exception occuring when the model is
        # loading on their servers.
        return_msg = f"Sorry, request failed at HuggingFace API. Reason: {e}"
        sendTelegramMessage(chat_id, return_msg)
        return

    # TODO 3: Handle other exceptions that could arise and inform the user with a message
    except:


startServerPolling(parseResponse)
