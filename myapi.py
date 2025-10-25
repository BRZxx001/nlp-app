from transformers import pipeline


class API:
    def __init__(self):
        # ==========================================================
        # --- MODEL INITIALIZATION ---
        # ==========================================================

        # Define model names
        model_sentiment = "distilbert-base-uncased-finetuned-sst-2-english"
        model_ner = "dslim/bert-base-NER"
        model_emotion = "j-hartmann/emotion-english-distilroberta-base"

        # Load Hugging Face pipelines
        self.classifier = pipeline("sentiment-analysis", model=model_sentiment)
        self.ner_tagger = pipeline("ner", model=model_ner, grouped_entities=True)
        self.emotion_analyzer = pipeline(
            "text-classification",
            model=model_emotion,
            return_all_scores=True
        )

    # ==========================================================
    # --- SENTIMENT ANALYSIS ---
    # ==========================================================
    def sentiment_analysis(self, text):
        """
        Perform Sentiment Analysis using pre-trained Hugging Face model.
        Returns a list with label (POSITIVE/NEGATIVE) and confidence score.
        """
        response = self.classifier(text)
        return response

    # ==========================================================
    # --- NAMED ENTITY RECOGNITION ---
    # ==========================================================
    def named_entity_recognition(self, text):
        """
        Perform Named Entity Recognition (NER).
        Returns entities like PERSON, ORG, LOC, etc., with confidence scores.
        """
        response = self.ner_tagger(text)
        return response

    # ==========================================================
    # --- EMOTION ANALYSIS ---
    # ==========================================================
    def emotion_analysis(self, text):
        """
        Perform Emotion Detection (like joy, sadness, anger, etc.)
        using a multi-label classification model.
        """
        response = self.emotion_analyzer(text)
        return response
