#modified open ALPR example code to quickly test the library and produce results
import os
import re
from openalpr import Alpr
from argparse import ArgumentParser

parser = ArgumentParser(description='OpenALPR Python Test Program')

parser.add_argument("-c", "--country", dest="country", action="store", default="eu",
                  help="License plate Country" )

parser.add_argument("--config", dest="config", action="store", default="/etc/openalpr/openalpr.conf",
                  help="Path to openalpr.conf config file" )

parser.add_argument("--runtime_data", dest="runtime_data", action="store", default="/usr/share/openalpr/runtime_data",
                  help="Path to OpenALPR runtime_data directory" )

parser.add_argument('plate_image', help='License plate image file')

options = parser.parse_args()

alpr = None
files = []
try:
    __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    alpr = Alpr("eu", options.config, options.runtime_data)

    if not alpr.is_loaded():
        print("Error loading OpenALPR")
    else:
        #print("Using OpenALPR " + alpr.get_version())
        files += [each for each in os.listdir('.') if each.endswith('.png')]
        print("<table>");
        for file in files:
            alpr.set_top_n(7)
            alpr.set_default_region("eu")
            alpr.set_detect_region(True)
            jpeg_bytes = open(__location__+file, "rb").read()
            results = alpr.recognize_array(jpeg_bytes)

            # Uncomment to see the full results structure
            # import pprint
            # pprint.pprint(results)

            #print("Image size: %dx%d" %(results['img_width'], results['img_height']))
            #print("Processing Time: %f" % results['processing_time_ms'])

            i = 0
            if(results['results']):
                print("<tr><td><img width='640' height='480' src='"+file+"' /></td><td>")
            for plate in results['results']:
                i += 1

                print("Plate #%d" % i)
                print("   %12s %12s" % ("Plate", "Confidence"))
                for candidate in plate['candidates']:
                     prefix = "-"
                     if candidate['matches_template']:
                         prefix = "*"

                     print("  %s %12s%12f" % (prefix, candidate['plate'], candidate['confidence']))
            if(results['results']):
                print("</td></tr>")
        print("</table>")


finally:
    if alpr:
        alpr.unload()
