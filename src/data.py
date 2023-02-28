class BasePipeline:
    def ingest(self):
        raise NotImplementedError

    def _preprocess(self):
        raise NotImplementedError

    def output(self):
        raise NotImplementedError


class InferencePipeline(BasePipeline):
    def __init__(self):
        print("Inference Pipeline initialized")

    def ingest(self, data):
        self._preprocess(data)

    def _preprocess(self, data):
        self.input_array = data[
            [
                "city_development_index",
                "gender",
                "relevent_experience",
                "enrolled_university",
                "education_level",
                "major_discipline",
                "experience",
                "company_size",
                "company_type",
                "last_new_job",
                "training_hours",
            ]
        ]

    def output(self):
        return self.input_array
