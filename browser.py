import webbrowser

def search_page(query: str):
#    urL = "https://www.skyscanner.com.tw/transport/flights/tnn/cai/230401/230430/?adults=1&adultsv2=1&cabinclass=economy&children=0&childrenv2=&destinationentityid=" + str(query) + "&inboundaltsenabled=false&infants=0&originentityid=33367910&outboundaltsenabled=true&preferdirects=false&ref=home&rtn=1"
    webbrowser.open_new(query)
