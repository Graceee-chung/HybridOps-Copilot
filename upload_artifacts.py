from src.azure_blob_utils import upload_file

upload_file("data/processed/cleaned_tickets.csv", "data/cleaned_tickets.csv")
upload_file("data/processed/tickets_with_priority.csv", "data/tickets_with_priority.csv")

upload_file("models/ticket_classifier.pkl", "models/ticket_classifier.pkl")
upload_file("models/priority_classifier.pkl", "models/priority_classifier.pkl")

upload_file("vector_store/ticket_faiss.index", "vector_store/ticket_faiss.index")
upload_file("vector_store/ticket_metadata.pkl", "vector_store/ticket_metadata.pkl")
upload_file("vector_store/kb_faiss.index", "vector_store/kb_faiss.index")
upload_file("vector_store/kb_metadata.pkl", "vector_store/kb_metadata.pkl")