import pandas as pd

pd.set_option('colheader_justify', 'center')   # FOR TABLE <th>

html_string = '''
<html>
  <head>
    <title>HTML Pandas Dataframe with CSS</title>
    <script src="https://www.kryogenix.org/code/browser/sorttable/sorttable.js"></script>
    <link rel="stylesheet" type="text/css" href="df_style.css"/> <!-- To add any additional custom css -->
  </head>
  <body>
    {table}
  </body>
</html>
'''

# creating the dataframe
df = pd.DataFrame({"Name": ['Anurag', 'Manjeet', 'Shubham',
                            'Saurabh', 'Ujjawal'],

                   "Address": ['Patna', 'Delhi', 'Coimbatore',
                               'Greater noida', 'Patna'],

                   "ID": [20123, 20124, 20145, 20146, 20147],

                   "Sell": [140000, 300000, 600000, 200000, 600000]})

with open('myhtml.html', 'w') as f:
    f.write(html_string.format(table=df.to_html(classes='sortable')))
