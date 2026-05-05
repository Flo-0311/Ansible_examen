import mysql.connector

def test_connection_database(host):
    try:
        conn = mysql.connector.connect(
        host="localhost",
        user="user",
        password="password",
        database="magento")
    except Exception as e:
        result = 1
        print({e})
    else:
        result = 0
    finally:
      conn.close()
    assert result == 0