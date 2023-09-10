import json

#Constants
JSON_FILE = "manifest-summary.json"
DYNAMO_DB_JSON = "manifest-files.json"
OUTPUT_FILE = "airline.bin"

# this is the manifast-files.json
# {"itemCount":8553,"md5Checksum":"TT/DHaVumCj3QoOhfm6/tg==","etag":"e11e560d0751aa5933630fb904f5d0df-1","dataFileS3Key":"public-s3-files/Output_Airline.csv/AWSDynamoDB/01693467621041-039fcf72/data/jhg6wb6v7u6dxdgwnn4c55ciq4.json.gz"}
# {"itemCount":8518,"md5Checksum":"AQVZBVs72EIIerVTiSqlJQ==","etag":"b617cfbf490266c83f1d395de22e37ff-1","dataFileS3Key":"public-s3-files/Output_Airline.csv/AWSDynamoDB/01693467621041-039fcf72/data/vpk7bsxd6e5ybiuwsn3de2nyyq.json.gz"}
# {"itemCount":8431,"md5Checksum":"2/5GNNeeGOj4tkPd4hfVGw==","etag":"905971bbb6d3e994da27740e68ab9102-1","dataFileS3Key":"public-s3-files/Output_Airline.csv/AWSDynamoDB/01693467621041-039fcf72/data/65bl37edfm3rrkcqdytwuecvsq.json.gz"}
# {"itemCount":8606,"md5Checksum":"1pGbTlAFuu9ySS4MKtrJ1Q==","etag":"8c42bb4e385197a959d58289c5b6b7e9-1","dataFileS3Key":"public-s3-files/Output_Airline.csv/AWSDynamoDB/01693467621041-039fcf72/data/vymh753xwiz5vftwknsj2yjh5i.json.gz"}
# {"itemCount":8670,"md5Checksum":"DxAOrBvD/rpuQN/BWsxAgA==","etag":"9b2db6d1738a3e8d257454c62168c4e2-1","dataFileS3Key":"public-s3-files/Output_Airline.csv/AWSDynamoDB/01693467621041-039fcf72/data/ylefrfhpaq6yrmxpak7bqikdtq.json.gz"}
# {"itemCount":8557,"md5Checksum":"HQDSqG/4HB2uZ12wnKlzzg==","etag":"f81e0f40536a03280f21e7c6065ed452-1","dataFileS3Key":"public-s3-files/Output_Airline.csv/AWSDynamoDB/01693467621041-039fcf72/data/xntpes3bre7wtpuidykki4mfiy.json.gz"}
# {"itemCount":8536,"md5Checksum":"Juy8kyHH9K6Zo+/U6BhIhQ==","etag":"0414f9b0ef186faa4dd9184c5769dbfa-1","dataFileS3Key":"public-s3-files/Output_Airline.csv/AWSDynamoDB/01693467621041-039fcf72/data/ozujwmfinuydrbb5l5xdvywljy.json.gz"}

# this is the manifest-summary.json
# {"version":"2020-06-30","exportArn":"arn:aws:dynamodb:us-east-1:531647909506:table/Airline/export/01693467621041-039fcf72","startTime":"2023-08-31T07:40:21.041Z","endTime":"2023-08-31T07:47:46.862Z","tableArn":"arn:aws:dynamodb:us-east-1:531647909506:table/Airline","tableId":"38148de1-7171-4ea4-85b2-e8b004fe4fe0","exportTime":"2023-08-31T07:40:21.041Z","s3Bucket":"ori-531647909506","s3Prefix":"public-s3-files/Output_Airline.csv","s3SseAlgorithm":"AES256","s3SseKmsKeyId":null,"manifestFilesS3Key":"public-s3-files/Output_Airline.csv/AWSDynamoDB/01693467621041-039fcf72/manifest-files.json","billedSizeBytes":0,"itemCount":59871,"outputFormat":"DYNAMODB_JSON"}

# this is one line of the json file
# {"Item":{"Passenger ID":{"N":"49010"},"Country Name":{"S":"China"},"Departure Date":{"S":"2/4/2022"},"Arrival Airport":{"S":"ZAT"},"Pilot Name":{"S":"Isak McCambrois"},"Last Name":{"S":"McCambrois"},"Continents":{"S":"Asia"},"First Name":{"S":"Isak"},"Flight Status":{"S":"Cancelled"},"Airport Name":{"S":"Zhaotong Airport"},"Gender":{"S":"Male"},"Airport Country Code":{"S":"CN"},"Airport Continent":{"S":"AS"},"Age":{"S":"69"},"Nationality":{"S":"Portugal"}}}

def create_bin_file():
    # create the output file
    output_file = open(OUTPUT_FILE, "wb")

    # extract the number of elements
    json_file = open(JSON_FILE, "r")
    json_file_data = json.load(json_file)
    num_elements = json_file_data["itemCount"]
    # write the size
    output_file.write(num_elements.to_bytes(8, byteorder='little'))
    # close the file
    json_file.close()

    # in the dynamo db json file, each line is a json object
    dynamo_db_json_file = open(DYNAMO_DB_JSON, "r", encoding="utf8")
    for line in dynamo_db_json_file:
        data = json.loads(line)
        # open the file and read the data
        file_name = data["dataFileS3Key"]
        # extract the file name
        file_name = file_name.split("/")[-1]
        # remove the ".gz" at the end
        file_name = file_name[:-3]
        # open the file
        curr_file = open(file_name, "r", encoding="utf8")
        for line_item in curr_file:
            # each line is a json object
            data_item = json.loads(line_item)
            # extract the item
            age = int(data_item["Item"]["Age"]["S"])
            # write the age to the file
            output_file.write(age.to_bytes(8, byteorder='little'))

        curr_file.close()

    dynamo_db_json_file.close()
    output_file.close()


def main():
    create_bin_file()


if __name__ == "__main__":
    main()