import azure.functions as func
import datetime
import json
import logging
import pickle
import pandas as pd


app = func.FunctionApp()

        
@app.route(route="score_model", auth_level=func.AuthLevel.ANONYMOUS)
def score_model(req: func.HttpRequest) -> func.HttpResponse:
    
    # Getting supplier and quantity from request
    supplier = req.params.get('supplier')
    quantity = req.params.get('quantity')
    warehouse = req.params.get('warehouse')
    product = req.params.get('product')
    quarter = req.params.get('quarter')
    holiday = req.params.get('holiday')
    days_between_order_and_delivery = req.params.get('days')
    
    # Load Model 
    model = pickle.load(open('./gbm_500.pkl', 'rb'))
    
    # Define the possible suppliers
    suppliers = ['Aromatico', 'Beans Inc.', 'Fair Trade AG', 'Farmers of Brazil', 'Handelskontor Hamburg']
    warehouses = ['Amsterdam - RR', 'Barcelona - RR', 'Hamburg - RR', 'Istanbul - RR', 'London - RR', 'Nairobi - RR', 'Naples - RR']
    products = ['Arabica', 'Excelsa', 'Liberica', 'Maragogype', 'Maragogype Type B', 'Robusta']
    quarters = ['Q1', 'Q2', 'Q3', 'Q4']
    # holidays = ['Yes', 'No']

    
    # Create a dictionary for the DataFrame
    data = {
        "total_qty": [quantity]
    }
    
    # Add supplier one-hot encoding to the dictionary
    for s in suppliers:
        data[f'd_{s}'] = [1 if s == supplier else 0]

    # Add warehouse one-hot encoding to the dictionary
    for w in warehouses:
        data[f'd_{w}'] = [1 if w == warehouse else 0]

    # Add product one-hot encoding to the dictionary
    for p in products:
        data[f'd_{p}'] = [1 if p == product else 0]

    # Add quarter one-hot encoding to the dictionary
    for q in quarters:
        data[f'd_{q}_order'] = [1 if q == quarter else 0]

    # Add holiday one-hot encoding to the dictionary for "is_holiday"
    data['is_holiday'] = [1 if holiday == 'Yes' else 0]

    # Add days_between_order_and_delivery to the dictionary
    data['days_between_order_and_delivery'] = [days_between_order_and_delivery]

    
    # Create the DataFrame
    payload = pd.DataFrame(data)

    # # Save the DataFrame to a CSV file
    # payload.to_csv('payload.csv', index=False)
    
    # Calculate the prediction
    prediction = model.predict(payload)[0]
    
    # Log the prediction
    logging.warning(f"Predictions: {prediction}") 
    
    return json.dumps({
        "message": f"""Model scored successfully! with quantity: {quantity}, supplier: {supplier}, product: {product}, warehouse: {warehouse}, quarter: {quarter}, holiday: {holiday}, and days between order and delivery {days_between_order_and_delivery} and the prediction is: {prediction}""",       
        "prediction": prediction,
        "status_code": 200
        })
        