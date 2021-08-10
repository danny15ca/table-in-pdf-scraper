import tabula
import argparse
import pandas as pd

print("\n*** Welcome to the program ***")
try:
    fileName = ""
    # Creating arguments passed from command line
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--file_path", help="path of the data file.")
    args = parser.parse_args()

    if args.file_path:
        fileName = args.file_path

    # Creating the first dataframe from the 1st page of the pdf file
    df1 = tabula.read_pdf(fileName,
                        pages="1")
    # Creating the second dataframe from the rest of the pdf file
    df2 = tabula.read_pdf(fileName,
                        pages="2-110",
                        multiple_tables=False,
                        pandas_options={
                            "header": None,
                            "names": [
                                "STT",
                                "Địa điểm phong toả",
                                "Quận/Huyện",
                                "Phường xã"]})
    # Concatnating two dataframe's
    result = pd.concat([df1[0], df2[0]])
    # Renaming columns of the result dataframe
    result.columns = ["ID", "Location", "District", "Ward"]
except Exception as e:
    print("\nSomething wrong happened. Error details:\n" + str(e))
    result = None

if result is not None:
    # Saving the result dataframe to CSV file
    try:
        output_path = input("\nEnter output path of output CSV file: ")
        result.to_csv(output_path, index=False)
        print("\nSuccessfully converted the pdf file to csv file.")
    except Exception as e:
        print("\nSorry, we cannot create a csv file. Please check your provided output path.\nError details:\n" + str(e))
    
    # Retrieving data from the dataframe by providing row index
    isInputValid = False
    isContinued = True
    print("\nNumber of records in our database: " + str(len(result)) + ".")
    while isContinued:
        while not isInputValid:
            try:
                row_idx = int(input("\nEnter row index you want to retrieve data: "))
                print("\nYour result:\n{0}".format(result.iloc[row_idx-1, :]))
                isInputValid = True
            except Exception as e:
                isInputValid = False
                print("\nSorry, your input is invalid.")
        usr_cont = input("\nDo you want to continue? (Y/N): ")
        if str(usr_cont).upper() == "N":
            isContinued = False
        else:
            isContinued = True
            isInputValid = False
    print("\nThank you for visiting my program :-)")
else:
    print("\nPlease recheck your data file.")
