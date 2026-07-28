from client import KnowledgeBaseQaClient

def main():
    client = KnowledgeBaseQaClient()
    res = client.search_kb(query='What is the vacation policy?')
    print(f"Result for answer: {res['answer']}")

if __name__ == "__main__":
    main()
