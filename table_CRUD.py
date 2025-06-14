#*************************#
#DPSK#2025.06.12#
import pymysql
from datetime import datetime
import traceback

class CRUDManager:
    def __init__(self, cursor, table_name):
        """
        初始化CRUD管理器
        
        参数:
            cursor: 数据库游标对象
            table_name (str): 数据库表名
        """
        self.cursor = cursor
        self.table_name = table_name
        self.column_types = {}
        self.column_names = []
        self.primary_key = ""
        self.setup_columns()
    
    def setup_columns(self):
        """设置表格列并存储列类型信息"""
        try:
            self.cursor.execute(f"DESCRIBE {self.table_name}")
            columns = self.cursor.fetchall()
            
            # 存储列类型信息
            self.column_types = {}
            self.column_names = [col[0] for col in columns]
            
            # 查找主键
            self.primary_key = ""
            for col in columns:
                col_name = col[0]
                col_type = col[1].upper()
                self.column_types[col_name] = col_type
                
                # 如果该列是主键
                if col[3] == "PRI":
                    self.primary_key = col_name
            
            # 如果没有明确的主键，则假设第一列是主键
            if not self.primary_key and self.column_names:
                self.primary_key = self.column_names[0]
                
        except pymysql.Error as e:
            print(f"获取表结构失败: {e}")
    
    def load_data(self, condition=None, params=None):
        """
        从数据库加载数据，可选条件
        
        参数:
            condition (str): SQL条件语句
            params (list): 条件参数列表
            
        返回:
            list: 查询结果列表
        """
        try:
            # 构建查询语句
            if condition:
                query = f"SELECT * FROM {self.table_name} WHERE {condition}"
                self.cursor.execute(query, params)
            else:
                query = f"SELECT * FROM {self.table_name}"
                self.cursor.execute(query)
            
            return self.cursor.fetchall()
            
        except pymysql.Error as e:
            print(f"加载数据失败: {e}")
            return []
    
    def update_data(self, row_data, primary_key_value):
        """
        更新单行数据
        
        参数:
            row_data (dict): 要更新的列数据 {列名: 值}
            primary_key_value: 主键值
            
        返回:
            bool: 更新是否成功
        """
        try:
            # 构建SET子句
            set_clause = []
            values = []
            
            for col_name, value in row_data.items():
                # 跳过主键列
                if col_name == self.primary_key:
                    continue
                    
                set_clause.append(f"`{col_name}` = %s")
                values.append(value)
            
            # 添加主键值
            values.append(primary_key_value)
            
            # 构建UPDATE语句
            update_query = f"""
                UPDATE `{self.table_name}` 
                SET {', '.join(set_clause)}
                WHERE `{self.primary_key}` = %s
            """
            
            # 执行更新
            self.cursor.execute(update_query, values)
            return True
                
        except pymysql.Error as e:
            error_info = f"MySQL错误 {e.args[0]}: {e.args[1]}"
            print(f"更新数据时出错: {error_info}")
            return False
        except Exception as e:
            error_trace = traceback.format_exc()
            print(f"发生未预期错误: {str(e)}\n\n{error_trace}")
            return False
    
    def delete_data(self, primary_key_values):
        """
        删除指定主键的数据
        
        参数:
            primary_key_values (list): 主键值列表
            
        返回:
            bool: 删除是否成功
        """
        if not primary_key_values:
            return False
            
        try:
            # 创建占位符字符串
            placeholders = ', '.join(['%s'] * len(primary_key_values))
            
            delete_query = f"""
                DELETE FROM `{self.table_name}`
                WHERE `{self.primary_key}` IN ({placeholders})
            """
            
            # 执行删除
            self.cursor.execute(delete_query, primary_key_values)
            return self.cursor.rowcount > 0
        
        except pymysql.Error as e:
            error_info = f"MySQL错误 {e.args[0]}: {e.args[1]}"
            print(f"删除记录时出错: {error_info}")
            return False
        except Exception as e:
            error_trace = traceback.format_exc()
            print(f"发生未预期错误: {str(e)}\n\n{error_trace}")
            return False
    
    def insert_data(self, row_data):
        """
        插入新数据
        
        参数:
            row_data (dict): 要插入的列数据 {列名: 值}
            
        返回:
            bool: 插入是否成功
        """
        try:
            # 构建INSERT语句
            columns = []
            placeholders = []
            values = []
            
            for col_name, value in row_data.items():
                columns.append(f"`{col_name}`")
                placeholders.append("%s")
                values.append(value)
            
            insert_query = f"""
                INSERT INTO `{self.table_name}` 
                ({', '.join(columns)})
                VALUES ({', '.join(placeholders)})
            """
            
            # 执行插入
            self.cursor.execute(insert_query, values)
            return True
                
        except pymysql.Error as e:
            error_info = f"MySQL错误 {e.args[0]}: {e.args[1]}"
            print(f"插入数据时出错: {error_info}")
            return False
        except Exception as e:
            error_trace = traceback.format_exc()
            print(f"发生未预期错误: {str(e)}\n\n{error_trace}")
            return False
    
    def search_data(self, field=None, keyword=None):
        """
        搜索数据
        
        参数:
            field (str): 搜索字段（None表示所有字段）
            keyword (str): 搜索关键词
            
        返回:
            list: 搜索结果
        """
        if not keyword:
            return self.load_data()
        
        # 构建搜索条件
        conditions = []
        params = []
        keyword_pattern = f"%{keyword}%"
        
        if field and field in self.column_names:
            # 搜索特定字段
            conditions.append(f"`{field}` LIKE %s")
            params.append(keyword_pattern)
        else:
            # 搜索所有字段
            for col in self.column_names:
                conditions.append(f"`{col}` LIKE %s")
                params.append(keyword_pattern)
        
        condition = " OR ".join(conditions)
        return self.load_data(condition, params)
#DPSK#