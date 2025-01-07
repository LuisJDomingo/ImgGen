print("inocio run")

from app import create_app

app = create_app()

'''@app.route('/debug')
def debug():
    return jsonify(routes=str(app.url_map), config=app.config)'''

if __name__ == '__main__':
    app.run(debug=True)
