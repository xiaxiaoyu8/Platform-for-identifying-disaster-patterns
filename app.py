from flask import Flask, render_template, jsonify, request, Blueprint
import json
import os
import time
import pandas as pd
from werkzeug.utils import secure_filename
from threading import Timer
import webbrowser
import sys

app = Flask(__name__)

data_bp = Blueprint('data', __name__)
app.register_blueprint(data_bp, url_prefix='/api/data')

# 当flage==0时,默认调用000_workbench.json等初始数据文件
# 当flage==1时,调用101_risk_identification copy.json
global flage
flage = 0

if getattr(sys, 'frozen', False):
    BASE_DIR = os.path.dirname(sys.executable)
else:
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    
app.config['JSON_AS_ASCII'] = False
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config['UPLOAD_FOLDER'] = os.path.join(BASE_DIR, 'uploads')
app.config['MAX_CONTENT_LENGTH'] = 8 * 1024 * 1024  # 8MB max file size

if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

# 工具函数:读取JSON数据
def load_json_data(filename):
    try:
        filepath = os.path.join('data', filename)
        with open(filepath, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        return {'error': f'文件 {filename} 不存在'}
    except json.JSONDecodeError:
        return {'error': f'文件 {filename} JSON格式错误'}

# 工具函数:保存JSON数据
def save_json_data(filename, data):
    try:
        filepath = os.path.join('data', filename)
        # 确保data目录存在
        if not os.path.exists('data'):
            os.makedirs('data')
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        return True
    except Exception as e:
        # print(f"保存文件失败: {e}")
        return False

# 主页路由
@app.route('/')
@app.route('/index')
def index():
    """首页 - 工作台"""
    return render_template('index.html')

# 工作台
@app.route('/workbench')
def workbench():
    """工作台"""
    data = load_json_data('000_workbench.json')
    return render_template('/pages/P000_workbench.html', data=data)

# 1XX系列
@app.route('/pages/P101_risk_identification.html')
def risk_identification():
    """风险识别"""    
    global flage
    if flage == 1:
        data = load_json_data('101_risk_identification copy.json')
    else:
        data = load_json_data('101_risk_identification.json')
    return render_template('/pages/P101_risk_identification.html', data=data)

@app.route('/pages/P102_risk_measurement.html')
def risk_measurement():
    """风险度量"""
    global flage
    if flage == 1:
        data = load_json_data('102_risk_measurement copy.json')
    else:
        data = load_json_data('102_risk_measurement.json')
    return render_template('/pages/P102_risk_measurement.html', data=data)

@app.route('/pages/P103_risk_strategy.html')
def risk_strategy():
    """风险策略"""
    global flage
    if flage == 1:
        data = load_json_data('103_risk_strategy copy.json')
    else:
        data = load_json_data('103_risk_strategy.json')
    return render_template('/pages/P103_risk_strategy.html', data=data)

@app.route('/pages/P104_risk_monitoring.html')
def risk_monitoring():
    """风险监控"""
    global flage
    if flage == 1:
        data = load_json_data('104_risk_monitoring copy.json')
    else:
        data = load_json_data('104_risk_monitoring.json')
    return render_template('/pages/P104_risk_monitoring.html', data=data)

# 2XX系列
@app.route('/pages/P201_disaster_collection.html')
def disaster_collection():
    """灾害采集"""
    global flage
    if flage == 1:
        data = load_json_data('201_disaster_collection copy.json')
    else:
        data = load_json_data('201_disaster_collection.json')
    return render_template('/pages/P201_disaster_collection.html', data=data)

@app.route('/pages/P202_disaster_trend_analysis.html')
def disaster_trend_analysis():
    """灾害趋势分析"""
    global flage
    if flage == 1:
        data = load_json_data('202_disaster_trend_analysis copy.json')
    else:
        data = load_json_data('202_disaster_trend_analysis.json')
    return render_template('/pages/P202_disaster_trend_analysis.html', data=data)

@app.route('/pages/P203_early_warning_level.html')
def early_warning_level():
    """预警等级设置"""
    global flage
    if flage == 1:
        data = load_json_data('203_early_warning_level copy.json')
    else:
        data = load_json_data('203_early_warning_level.json')
    return render_template('/pages/P203_early_warning_level.html', data=data)

@app.route('/pages/P204_early_warning_channel.html')
def early_warning_channel():
    """预警发布渠道"""
    global flage
    if flage == 1:
        data = load_json_data('204_early_warning_channel copy.json')
    else:
        data = load_json_data('204_early_warning_channel.json')
    return render_template('/pages/P204_early_warning_channel.html', data=data)

@app.route('/pages/P205_risk_score.html')
def risk_score():
    """风险评分"""
    global flage
    if flage == 1:
        data = load_json_data('205_risk_score copy.json')
    else:
        data = load_json_data('205_risk_score.json')
    return render_template('/pages/P205_risk_score.html', data=data)

# 3XX系列
@app.route('/pages/P301_model_construction.html')
def model_construction():
    """模型构建"""
    global flage
    if flage == 1:
        data = load_json_data('301_model_construction copy.json')
    else:
        data = load_json_data('301_model_construction.json')
    return render_template('/pages/P301_model_construction.html', data=data)

@app.route('/pages/P302_model_verification.html')
def model_verification():
    """模型验证"""
    global flage
    if flage == 1:
        data = load_json_data('302_model_verification copy.json')
    else:
        data = load_json_data('302_model_verification.json')
    return render_template('/pages/P302_model_verification.html', data=data)

@app.route('/pages/P303_model_optimization.html')
def model_optimization():
    """模型优化"""
    global flage
    if flage == 1:
        data = load_json_data('303_model_optimization copy.json')
    else:
        data = load_json_data('303_model_optimization.json')
    return render_template('/pages/P303_model_optimization.html', data=data)

@app.route('/pages/P304_model_application.html')
def model_application():
    """模型应用"""
    data = load_json_data('304_model_application.json')
    return render_template('/pages/P304_model_application.html', data=data)

# 4XX系列
@app.route('/pages/P401_user_permission.html')
def user_permission():
    """用户权限"""
    data = load_json_data('401_user_permission.json')
    return render_template('/pages/P401_user_permission.html', data=data)

@app.route('/pages/P402_system_config.html')
def system_config():
    """系统配置"""
    data = load_json_data('402_system_config.json')
    return render_template('/pages/P402_system_config.html', data=data)

@app.route('/pages/P403_system_backup.html')
def system_backup():
    """系统备份"""
    data = load_json_data('403_system_backup.json')
    return render_template('/pages/P403_system_backup.html', data=data)

@app.route('/pages/P404_system_troubleshooting.html')
def system_troubleshooting():
    """故障排除"""
    data = load_json_data('404_system_troubleshooting.json')
    return render_template('/pages/P404_system_troubleshooting.html', data=data)

# API路由 - 用于动态获取JSON数据
@app.route('/api/data/<filename>')
def get_data(filename):
    """API接口:获取指定JSON文件数据"""
    data = load_json_data(filename)
    return jsonify(data)

# ================= 修改指标路由 =================
@app.route('/api/data/<data_key>/update/<int:index>', methods=['POST'])
def update_data(data_key, index):
    # print(f"收到修改请求，索引: {index}, 数据: {request.json}")
    try:
        updated_item = request.json
        json_file = data_key.replace('P', '', 1) + '.json'
        data = load_json_data(json_file)
        # print(f"当前数据长度: {len(data)}")

        if index < 0 or index >= len(data):
            return jsonify({"success": False, "message": "索引越界"}), 400

        data[index] = updated_item
        save_json_data(json_file, data)
        # print(f"修改成功，当前数据长度: {len(data)}")

        return jsonify({"success": True, "message": "修改成功"})

    except Exception as e:
        return jsonify({"success": False, "message": str(e)}), 500

# ================= 删除指标路由 =================
# 约定：data_key -> json 文件名
# P101_risk_identification -> 101_risk_identification.json
@app.route('/api/data/<data_key>/delete/<int:index>', methods=['POST'])
def delete_data(data_key, index):
    # print(f"收到删除请求 data_key={data_key}, index={index}")
    try:
        json_file = data_key.replace('P', '', 1) + '.json'
        # print(f"映射 JSON 文件: {json_file}")
        data = load_json_data(json_file)
        # print(f"当前数据长度: {len(data)}")
        if index < 0 or index >= len(data):
            return jsonify({"success": False, "message": "索引越界"}), 400

        data.pop(index)   # 关键操作
        save_json_data(json_file, data)
        # print(f"删除成功，当前数据长度: {len(data)}")
        return jsonify({"success": True, "message": "删除成功"})

    except Exception as e:
        return jsonify({"success": False, "message": str(e)}), 500

# ================= 新增信息路由 =================
@app.route('/api/data/<data_key>/add', methods=['POST'])
def add_data(data_key):
    # print(f"收到新增请求，数据: {request.json}")
    try:
        json_file = data_key.replace('P', '', 1) + '.json'
        new_item = request.json
        if not new_item:
            return jsonify(success=False, message='数据为空')
        data = load_json_data(json_file)
        # print(f"当前数据长度: {len(data)}")
        data.append(new_item)
        save_json_data(json_file, data)
        # print(f"新增成功，当前数据长度: {len(data)}")
        return jsonify({"success": True, "message": "新增成功"})

    except Exception as e:
        return jsonify({"success": False, "message": str(e)}), 500

# 数据导入API 304_model_application
@app.route('/api/import/304_model_application', methods=['POST'])
def import_model_application_data():
    """导入Excel文件并解析为JSON，保存到 data/304_model_application.json"""
    try:
        # 1. 检查是否有文件部分
        if 'file' not in request.files:
            return jsonify({'success': False, 'message': '未找到上传的文件部分'})
        file = request.files['file']

        # 2. 检查是否选择了文件
        if file.filename == '':
            return jsonify({'success': False, 'message': '未选择任何文件'})

        # 3. 检查文件扩展名
        if not file.filename.lower().endswith(('.xlsx', '.xls')):
            return jsonify({'success': False, 'message': '只支持 .xlsx 或 .xls 格式的Excel文件'})

        # 4. 安全生成文件名并保存到临时上传目录
        filename = secure_filename(file.filename)
        if not filename:  # 极少见的安全过滤后为空的情况
            return jsonify({'success': False, 'message': '文件名无效'})
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)

        # 5. 读取Excel文件
        try:
            df = pd.read_excel(filepath)
        except Exception as read_error:
            os.remove(filepath)  # 读取失败也清理临时文件
            return jsonify({'success': False, 'message': f'读取Excel文件失败: {str(read_error)}'})

        # 6. 检查数据是否为空
        if df.empty:
            os.remove(filepath)
            return jsonify({'success': False, 'message': 'Excel文件中没有数据'})

        # 7. 转换为列表字典格式（records）
        data_list = df.to_dict(orient='records')

        # 8. 保存到 data/304_model_application.json（覆盖式）
        if save_json_data('304_model_application.json', data_list):
            if os.path.exists(filepath):
                os.remove(filepath)
                flage = 0  # 表示数据未更新
                #两秒延时
                time.sleep(1)
            return jsonify({
                'success': True,
                'message': f'成功处理 {len(data_list)} 条数据，已保存到数据库!',
                'count': len(data_list)
            })
        else:
            if os.path.exists(filepath):
                os.remove(filepath)
            return jsonify({'success': False, 'message': '数据保存到JSON文件失败'})
    except Exception as e:
        if 'filepath' in locals() and os.path.exists(filepath):
            try:
                os.remove(filepath)
            except:
                pass
        return jsonify({'success': False, 'message': f'导入过程出错: {str(e)}'})

# 数据导入API 205_risk_score
@app.route('/api/import/205_risk_score', methods=['POST'])
def import_risk_score_data():
    """导入Excel文件并解析为JSON，保存到 data/205_risk_score.json"""
    try:
        # 1. 检查是否有文件部分
        if 'file' not in request.files:
            return jsonify({'success': False, 'message': '未找到上传的文件部分'})
        file = request.files['file']

        # 2. 检查是否选择了文件
        if file.filename == '':
            return jsonify({'success': False, 'message': '未选择任何文件'})

        # 3. 检查文件扩展名
        if not file.filename.lower().endswith(('.xlsx', '.xls')):
            return jsonify({'success': False, 'message': '只支持 .xlsx 或 .xls 格式的Excel文件'})

        # 4. 安全生成文件名并保存到临时上传目录
        filename = secure_filename(file.filename)
        if not filename:  # 极少见的安全过滤后为空的情况
            return jsonify({'success': False, 'message': '文件名无效'})
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)

        # 5. 读取Excel文件
        try:
            df = pd.read_excel(filepath)
        except Exception as read_error:
            os.remove(filepath)  # 读取失败也清理临时文件
            return jsonify({'success': False, 'message': f'读取Excel文件失败: {str(read_error)}'})

        # 6. 检查数据是否为空
        if df.empty:
            os.remove(filepath)
            return jsonify({'success': False, 'message': 'Excel文件中没有数据'})

        # 7. 转换为列表字典格式（records）
        data_list = df.to_dict(orient='records')

        # 8. 保存到 data/205_risk_score.json（覆盖式）
        if save_json_data('205_risk_score.json', data_list):
            if os.path.exists(filepath):
                os.remove(filepath)
                #两秒延时
                time.sleep(1)
                # risk_evaluation = "危险值大于0.8，须尽快撤离"
                pattern = "灾害模式已识别"
                
                # 可以根据data_list中的数据进行实际计算
                if data_list:
                    # avg_risk = sum(item.get('risk_value', 0) for item in data_list) / len(data_list)
                    #获取后端json的第一个数据
                    avg_risk = data_list[0].get('P', 0)# p == 0.3
                    if avg_risk > 0.4:
                        risk_evaluation = f"危险值{avg_risk:.2f}，大于0.8，须尽快撤离"
                    else:
                        risk_evaluation = f"危险值{avg_risk:.2f}，暂无紧急风险"
            
            return jsonify({
                'success': True,
                'message': f'成功处理 {len(data_list)} 条数据，已保存到数据库!',
                'count': len(data_list),
                'pattern': pattern,
                'risk_evaluation': risk_evaluation
            })
        else:
            if os.path.exists(filepath):
                os.remove(filepath)
            return jsonify({'success': False, 'message': '数据保存到JSON文件失败'})
    except Exception as e:
        if 'filepath' in locals() and os.path.exists(filepath):
            try:
                os.remove(filepath)
            except:
                pass
        return jsonify({'success': False, 'message': f'导入过程出错: {str(e)}'})

# 数据导入API 104_risk_monitoring
@app.route('/api/import/104_risk_monitoring', methods=['POST'])
def import_risk_monitoring_data():
        # 1. 检查是否有文件部分
        if 'file' not in request.files:
            return jsonify({'success': False, 'message': '未找到上传的文件部分'})
        file = request.files['file']

        # 2. 检查是否选择了文件
        if file.filename == '':
            return jsonify({'success': False, 'message': '未选择任何文件'})

        # 3. 检查文件扩展名
        if not file.filename.lower().endswith(('.xlsx', '.xls')):
            return jsonify({'success': False, 'message': '只支持 .xlsx 或 .xls 格式的Excel文件'})

        # 4. 安全生成文件名并保存到临时上传目录
        filename = secure_filename(file.filename)
        if not filename:  # 极少见的安全过滤后为空的情况
            return jsonify({'success': False, 'message': '文件名无效'})
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)

        # 5. 读取Excel文件
        try:
            df = pd.read_excel(filepath)
        except Exception as read_error:
            os.remove(filepath)  # 读取失败也清理临时文件
            return jsonify({'success': False, 'message': f'读取Excel文件失败: {str(read_error)}'})

        # 6. 检查数据是否为空
        if df.empty:
            os.remove(filepath)
            return jsonify({'success': False, 'message': 'Excel文件中没有数据'})

        # 7. 转换为列表字典格式（records）
        data_list = df.to_dict(orient='records')

        # 8. 保存到 data/104_risk_monitoring.json（覆盖式）
        if save_json_data('104_risk_monitoring.json', data_list):
            if os.path.exists(filepath):
                os.remove(filepath)
                #两秒延时
                # time.sleep(1)
                # risk_evaluation = "危险值大于0.8，须尽快撤离"
                pattern = "灾害模式已识别"
                
                # 可以根据data_list中的数据进行实际计算
                if data_list:
                    avg_risk = data_list[0].get('P', 0)# p == 0.3
                    if avg_risk > 0.4:
                        risk_evaluation = f"危险值{avg_risk:.2f}，大于0.8，须尽快撤离"
                    else:
                        risk_evaluation = f"危险值{avg_risk:.2f}，暂无紧急风险"
            
            return jsonify({
                'success': True,
                'message': f'成功处理 {len(data_list)} 条数据，已保存到数据库!',
                'count': len(data_list),
                'pattern': pattern,
                'risk_evaluation': risk_evaluation
            })
        else:
            if os.path.exists(filepath):
                os.remove(filepath)
            return jsonify({'success': False, 'message': '数据保存到JSON文件失败'})
    # except Exception as e:
    #     if 'filepath' in locals() and os.path.exists(filepath):
    #         try:
    #             os.remove(filepath)
    #         except:
    #             pass
        return jsonify({'success': False, 'message': f'导入过程出错: {str(e)}'})

# 错误处理
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(e):
    return render_template('500.html'), 500

def open_browser():
    webbrowser.open('http://127.0.0.1:5000')

# 启动应用
if __name__ == '__main__':
    # print(f"程序运行目录: {BASE_DIR}")
    # # print(f"数据目录: {DATA_DIR}")
    # print("正在启动服务器...")
    Timer(1.5, open_browser).start()
    app.run(host='127.0.0.1', port=5000, debug=False)