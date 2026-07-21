inventory_tool =     {
    "type": "function",
    "function": {
        "name": "get_inventory",
        "description": "Returns inventory for a product.",
        "parameters": {
            "type": "object",
            "properties": {
                "product": {
                    "type": "string",
                    "description": "The name of the product."
                }
            },
            "required": ["product"]
        }
    }
}

inventory_report_tool =     {
    "type": "function",
    "function": {
        "name": "get_inventory_report",
        "description": "Returns a report of the current inventory.",
        "parameters": {
            "type": "object",
            "properties": {},
            "required": []
        }
    }
}

revenue_tool = {
    "type": "function",
    "function" : {
        "name": "get_total_revenue",
        "description": "Returns the total revenue.",
        "parameters": {
            "type": "object",
            "properties": {},
            "required": []
        }
    }
}

top_product_tool = {
        "type": "function",
    "function" : {
        "name": "get_top_product",
        "description": "Returns the top-selling product.",
        "parameters": {
            "type": "object",
            "properties": {},
            "required": []
        }
    }
}

email_tool = {
        "type" : "function",
    "function" : {
        "name": "send_email",
        "description": "send email to a recipient with a message",
        "parameters" : {
            "type" : "object",
            "properties" : {
                "recipient":{
                    "type" : "string",
                    "description" : "The email address of the recipient."
                },
                "message" : {
                    "type" : "string",
                    "description" : "The message to be sent in the email."
                }
            },
            "required" : ["recipient", "message"]
        }
    }
}

tools = [
    inventory_tool,
    inventory_report_tool,
    revenue_tool,
    top_product_tool,
    email_tool
]