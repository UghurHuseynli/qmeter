from django.http import JsonResponse
from django.views import View
from pymongo import MongoClient
from django.conf import settings

class FeedbackView(View):
    def get(self, request):
        client = MongoClient(settings.MONGO_CLIENT)
        db = client[settings.MONGO_NAME]
        collection = db[settings.MONGO_COLLECTION]

        pipeline = [
            {"$unwind": "$feedback_rate"},
            {
                "$project": {
                    "branch_name": "$branch.name",
                    "service_name": "$feedback_rate.service.name",
                    "rate_option": "$feedback_rate.rate_option",
                }
            },
            {
                "$group": {
                    "_id": {
                        "branch_name": "$branch_name",
                        "service_name": "$service_name"
                    },
                    "count_1": {"$sum": {"$cond": [{"$eq": ["$rate_option", 1]}, 1, 0]}},
                    "count_2": {"$sum": {"$cond": [{"$eq": ["$rate_option", 2]}, 1, 0]}},
                    "count_3": {"$sum": {"$cond": [{"$eq": ["$rate_option", 3]}, 1, 0]}},
                    "count_4": {"$sum": {"$cond": [{"$eq": ["$rate_option", 4]}, 1, 0]}},
                    "count_5": {"$sum": {"$cond": [{"$eq": ["$rate_option", 5]}, 1, 0]}},
                }
            },
            {
                "$addFields": {
                    "numerator": {
                        "$add": [
                            {"$multiply": ["$count_1", 10]},
                            {"$multiply": ["$count_2", 5]},
                            {"$multiply": ["$count_3", 0]},
                            {"$multiply": ["$count_4", -5]},
                            {"$multiply": ["$count_5", -10]},
                        ]
                    },
                    "denominator": {
                        "$multiply": [
                            {
                                "$add": [
                                    "$count_1",
                                    "$count_2",
                                    "$count_3",
                                    "$count_4",
                                    "$count_5",
                                ]
                            },
                            10,
                        ]
                    },
                }
            },
            {
                "$addFields": {
                    "score": {
                        "$cond": {
                            "if": {"$ne": ["$denominator", 0]},
                            "then": {
                                "$multiply": [
                                    {"$divide": ["$numerator", "$denominator"]},
                                    100,
                                ]
                            },
                            "else": 0,
                        }
                    }
                }
            },
            {
                "$group": {
                    "_id": "$_id.branch_name",
                    "services": {
                        "$push": {
                            "name": "$_id.service_name",
                            "score": {"$round": ["$score", 2]},
                        }
                    },
                }
            },
            {
                "$project": {
                    "_id": 0,
                    "branch": "$_id",
                    "services": 1,
                }
            },
        ]
        feedback_data = list(collection.aggregate(pipeline))

        return JsonResponse(feedback_data, safe=False)

class FeedbackWithoutModelView(View):
        def get(self, request):
            client = MongoClient('mongodb://localhost:27017/')
            db = client['qmeter1']
            collection = db['user']

            # Define the MongoDB aggregation pipeline
            pipeline = [
                {"$unwind": "$feedback_rate"},
                {
                    "$project": {
                        "branch_name": "$branch.name",
                        "service_name": "$feedback_rate.service.name",
                        "rate_option": "$feedback_rate.rate_option",
                    }
                },
                {
                    "$group": {
                        "_id": {
                            "branch_name": "$branch_name",
                            "service_name": "$service_name"
                        },
                        "count_1": {"$sum": {"$cond": [{"$eq": ["$rate_option", 1]}, 1, 0]}},
                        "count_2": {"$sum": {"$cond": [{"$eq": ["$rate_option", 2]}, 1, 0]}},
                        "count_3": {"$sum": {"$cond": [{"$eq": ["$rate_option", 3]}, 1, 0]}},
                        "count_4": {"$sum": {"$cond": [{"$eq": ["$rate_option", 4]}, 1, 0]}},
                        "count_5": {"$sum": {"$cond": [{"$eq": ["$rate_option", 5]}, 1, 0]}},
                    }
                },
                {
                    "$addFields": {
                        "numerator": {
                            "$add": [
                                {"$multiply": ["$count_1", 10]},
                                {"$multiply": ["$count_2", 5]},
                                {"$multiply": ["$count_3", 0]},
                                {"$multiply": ["$count_4", -5]},
                                {"$multiply": ["$count_5", -10]},
                            ]
                        },
                        "denominator": {
                            "$multiply": [
                                {
                                    "$add": [
                                        "$count_1",
                                        "$count_2",
                                        "$count_3",
                                        "$count_4",
                                        "$count_5",
                                    ]
                                },
                                10,
                            ]
                        },
                    }
                },
                {
                    "$addFields": {
                        "score": {
                            "$cond": {
                                "if": {"$ne": ["$denominator", 0]},
                                "then": {
                                    "$multiply": [
                                        {"$divide": ["$numerator", "$denominator"]},
                                        100,
                                    ]
                                },
                                "else": 0,
                            }
                        }
                    }
                },
                {
                    "$group": {
                        "_id": "$_id.branch_name",
                        "services": {
                            "$push": {
                                "name": "$_id.service_name",
                                "score": {"$round": ["$score", 2]},
                            }
                        },
                    }
                },
                {
                    "$project": {
                        "_id": 0,
                        "branch": "$_id",
                        "services": 1,
                    }
                },
            ]

            # Execute the aggregation query
            feedback_data = list(collection.aggregate(pipeline))

            # Return the result as JSON
            return JsonResponse(feedback_data, safe=False)
            
