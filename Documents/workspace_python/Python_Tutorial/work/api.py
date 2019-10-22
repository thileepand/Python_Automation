import flask
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True

# Create Retailer Master.
RetailerMaster = [
            { "RetailerId":"478",
                "RetailerCode":"Thileep-DistR0001",
                "RetailerName": "stone store",
                "BeatId":0,
                "CreditLimit":0,
                "TinNumber":789,
                "ChannelId":430,
                "ClassId":463,
                "SubChannelId":432,
                "VisitFrequency":818,
                "RPTypeId":689,
                "WalkingSequence":0,
                "RField2":"",
                "RField3":0,
                "VisitDays":0,
                "radius":0,
                "RetCreditLimit":52,
                "AccountId":0,
                "RField1":0,
                "TaxTypeId":0,
                "RField4":301,
                "Locationid":"N",
                "IsDeadStore":"",
                "NfcTagId":0,
                "ContractStatusLovId":"",
                "CreditPeriod":"",
                "RField5":"",
                "RField6":"",
                "RField7":"",
                "SalesType":"",
                "ProfileImagePath":"",
                "GSTNumber":"",
                "InSEZ":"",
                "IsSameZone":"",
                "TinExpDate":"",
                "DLNo":"",
                "DLNoExpDate":876950,
                "SubDId":0,
                "pan_number":"",
                "food_licence_number":"",
                "food_licence_exp_date":"",
                "retailerTaxLocId":"31"
     },
]


# A route to return all of the available entries in our catalog.
@app.route('/api/RetailerMaster/', methods=['GET'])
def api_all():
    return jsonify(RetailerMaster)

if __name__ == '__main__':

    app.run(port=5000)