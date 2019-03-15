import os
from flask import Flask
from cfenv import AppEnv
from hdbcli import dbapi


app = Flask(__name__)
env = AppEnv()

port = int(os.environ.get('PORT', 3000))
hana = env.get_service(label='myhana')


@app.route('/')
def hello():
    # conn = dbapi.connect(address=hana.credentials['host'], port=int(hana.credentials['port']), user=hana.credentials['user'], password=hana.credentials['password'])
    conn = dbapi.connect(address="10.253.93.93", port=30041, user="SBSS_42736004359109273213610733685725394479282519476140875009139718622", password="To9AIS0Z.QI-8NTRgyupKWonDKUmI8_5aZ9eCNtk6MnTOM8rwKwQ1It20FZnFZskVNhGo5JCBCSQAnCpZ6LZms0Odidhk3OFzXJHg6CBHMViPEZbeT7Y62YTtirfUeuu")
    cursor = conn.cursor()
    cursor.execute("select CURRENT_UTCTIMESTAMP from DUMMY", {})
    ro = cursor.fetchone()
    cursor.close()
    conn.close()

    return "Current time is: " + str(ro["CURRENT_UTCTIMESTAMP"])


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port)