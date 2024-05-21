from app import app, render_template, session ,LWork_conn,LWork_cursor,LWork_lock
from flask import jsonify, request

# 啟用會員頁面
@app.route('/activate', methods=['GET', 'POST'])
def activate():
    # [ex]檢測 是否已付款
    member_id = session.get('UserID')
    item_id=1
    LWork_cursor.execute('SELECT id FROM Purchases WHERE Member_id = ? AND ShopItem_id = ?', (member_id, item_id))
    result = LWork_cursor.fetchone()
    if not result:
        return f'您尚未購買{item_id}'

    if request.method == 'POST':
         
        hwid = request.form['hwid']
        item_id = request.form['item_id']
        if not member_id:
            return '未登入'
        
        result = activate_hwid(member_id, hwid, item_id)
        #if result:
        return result
        #else:
        #    return 'HWID不存在'
    return render_template('Activate.html')


# 測試會員新增指定 HWID
def activate_hwid(member_id, hwid, item_id):
    LWork_cursor.execute('SELECT id,Activated FROM ActivationCodes WHERE HWID = ?', (hwid,))
    result = LWork_cursor.fetchone()
    if result:
        if result[1] == 1:
            return f'錯誤：{hwid} 已是起用狀態'
        with LWork_lock:
            LWork_conn.execute('INSERT INTO MemberHWID (Member_id, Item_id, HWID) VALUES (?, ?, ?)', (member_id, item_id, hwid))
            LWork_conn.execute('UPDATE ActivationCodes SET Activated = 1 WHERE HWID = ?', (hwid,))
            LWork_conn.commit()

        return f'{hwid} 啟用成功'
    else:

        return f'錯誤：HWID不存在'
    

# 測試會員移除指定 HWID
def deactivate_hwid(member_id, hwid):

    LWork_conn.execute('DELETE FROM MemberHWID WHERE Member_id = ? AND HWID = ?', (member_id, hwid))
    LWork_conn.execute('UPDATE ActivationCodes SET Activated = 0 WHERE HWID = ?', (hwid,))
    LWork_conn.commit()

# 測試查詢 HWID
def query_hwid_info(hwid):

    LWork_cursor.execute('SELECT Activated, ExpiryDate FROM ActivationCodes WHERE HWID = ?', (hwid,))
    result = LWork_cursor.fetchone()

    if result:
        activated, expiry_date = result

        return {'HWID': hwid, 'ExpiryDate': expiry_date, 'Activated': bool(activated)}
    else:

        return None

