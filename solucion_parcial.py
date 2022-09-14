class SolucionParcial:
    def __init__(self):
        self.diccionario_parcial = {}
    
    def feature_1_parcial(self):
        self.diccionario_parcial = {
            "DueDate": "2022-02-24",
            "Balance": 1990.19,
            "DocNumber": "1053811422",
            "Status": "Payable",
            "Line": [
                {
                "Description": "Sample Expense",
                "Amount": 500,
                "DetailType": "ExpenseDetail",
                "ExpenseDetail": {
                    "Customer": {
                            "value": "ABC123",
                            "name": "Sample Customer",
                            "Ref": {
                                "value": "DEF234",
                                "name": "Sample Construction",
                                "Address": ("Manizales",[170002, 170001, 170003, 170004])
                            }
                    },
                    "LineStatus": "Billable"
                }
                }
            ],
            "TotalAmt": 1990.19
            }


    def feature_2_parcial(self):
        print(self.diccionario_parcial["Line"][0]["ExpenseDetail"]["Customer"]["Ref"]["name"])