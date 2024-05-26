from bs4 import BeautifulSoup

def uprx_get_task(driver) -> dict:
    result:dict ; result = {}
    # ページのソースコードを取得
    html = driver.page_source

    # BeautifulSoupオブジェクトを作成してHTMLを解析
    soup = BeautifulSoup(html, 'html.parser')

    # 'signPortal signPortalKadai'クラスを持つすべてのspanタグを探す
    kadai_spans = soup.find_all('span', class_='signPortal signPortalKadai')

    i:int ; i = 1
    for kadai_span in kadai_spans:
        # kadai_spanの親がpタグでないことを確認
        if kadai_span.parent.name != 'p':
            # 各kadai_spanの次の兄弟要素をチェック
            date_span = kadai_span.find_next_sibling('span', class_='textDate')
            task_link = kadai_span.find_next_sibling('a', class_='ui-commandlink ui-widget textTitle')
            
            if date_span and task_link:
                date_text = date_span.text
                task_title = task_link.text
                print(f"日付: {date_text}, タイトル: {task_title}")

                result[i]["date"] = date_span.text
                result[i]["title"] = task_title.text

                i += 1

            else:
                print("必要な情報が見つかりません。")
        else:
            print("pタグ内の要素は無視されました。")

    return result