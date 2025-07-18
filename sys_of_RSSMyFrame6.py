import wx
import sys_of_RSS
from table_CRUD import CRUDManager
import wx.dataview as dv

class sys_of_RSSMyFrame6(sys_of_RSS.MyFrame6):
    def __init__(self, parent, cursor):
        super().__init__(parent)
        self.cursor = cursor
        
        # 初始化CRUD管理器
        if self.cursor:
            self.crud_manager = CRUDManager(self.cursor, "employee_copy1")
        else:
            wx.MessageBox("数据库连接未初始化", "错误", wx.OK | wx.ICON_ERROR)
            return
        
        # 初始化选择状态
        self.selected_rows = set()
        
        # 设置表格列
        self.setup_columns()
        
        # 加载数据
        self.load_data_from_db()
        
        # 更新搜索下拉框
        self.update_search_choices()
        
        # 绑定事件
        self.Bind(dv.EVT_DATAVIEW_ITEM_VALUE_CHANGED, self.on_item_value_changed, self.m_dataViewListCtrl1)
        self.Bind(dv.EVT_DATAVIEW_SELECTION_CHANGED, self.on_selection_changed, self.m_dataViewListCtrl1)
        
        # 按钮事件绑定
        self.m_button30.Bind(wx.EVT_BUTTON, self.on_edit)  # 保存修改
        self.m_button31.Bind(wx.EVT_BUTTON, self.OnDeleteEmployee)  # 删除选中行
        self.m_button29.Bind(wx.EVT_BUTTON, self.add_employee)  # 添加员工
        self.m_button32.Bind(wx.EVT_BUTTON, self.on_search_table)  # 搜索功能
        self.m_button34.Bind(wx.EVT_BUTTON, self.cancel_selection)  # 取消选择
        self.m_button341.Bind(wx.EVT_BUTTON, self.load_data)  # 刷新数据
    
    def setup_columns(self):
        """设置表格列"""
        # 清空现有列
        while self.m_dataViewListCtrl1.GetColumnCount() > 0:
            self.m_dataViewListCtrl1.DeleteColumn(0)
        
        # 添加选择列
        self.m_dataViewListCtrl1.AppendToggleColumn("选择", width=30)
        
        # 添加数据列
        for col_idx, col_name in enumerate(self.crud_manager.column_names, start=1):
            self.m_dataViewListCtrl1.AppendTextColumn(col_name, width=wx.COL_WIDTH_AUTOSIZE)
    
    def on_item_value_changed(self, event):
        """处理复选框状态变化事件"""
        item = event.GetItem()
        col = event.GetColumn()
        row = self.m_dataViewListCtrl1.ItemToRow(item)
        
        # 只处理第一列（复选框列）
        if col == 0 and row != wx.NOT_FOUND:
            # 获取复选框状态
            checked = self.m_dataViewListCtrl1.GetToggleValue(row, 0)
            
            # 更新选择状态
            if checked:
                self.selected_rows.add(row)
            else:
                if row in self.selected_rows:
                    self.selected_rows.remove(row)
            
            # 更新按钮状态
            self.update_status()
    
    def on_selection_changed(self, event):
        """处理行选择变化事件"""
        # 清除所有选择
        self.m_dataViewListCtrl1.UnselectAll()
    
    def update_search_choices(self):
        """更新搜索下拉框选项"""
        self.m_choice2.Clear()
        self.m_choice2.Append("所有字段")
        for col_name in self.crud_manager.column_names:
            self.m_choice2.Append(col_name)
        if self.m_choice2.GetCount() > 0:
            self.m_choice2.SetSelection(0)
    
    def load_data_from_db(self, condition=None, params=None):
        """加载数据到表格"""
        # 清空现有数据
        self.m_dataViewListCtrl1.DeleteAllItems()
        self.selected_rows.clear()
        
        # 获取数据
        if condition and params:
            data = self.crud_manager.load_data(condition, params)
        else:
            data = self.crud_manager.load_data()
        
        # 填充数据
        for row in data:
            # 添加一行，第一列是复选框（初始未选中）
            self.m_dataViewListCtrl1.AppendItem([False] + [str(value) if value is not None else "" for value in row])
        
        # 更新状态
        self.update_status()
    
    def update_status(self):
        """更新状态信息"""
        selected_count = len(self.selected_rows)
        
        # 更新按钮状态
        self.m_button30.Enable(selected_count > 0)  # 保存修改按钮
        self.m_button31.Enable(selected_count > 0)  # 删除选中行按钮
    
    def get_selected_ids(self):
        """获取选中行的ID"""
        selected_ids = []
        for row in self.selected_rows:
            # 获取ID列（第二列）
            employee_id = self.m_dataViewListCtrl1.GetTextValue(row, 1)
            selected_ids.append(employee_id)
        return selected_ids
    
    def add_employee(self, event):
        """添加员工"""
        dlg = wx.TextEntryDialog(self, "请输入员工姓名", "添加员工")
        if dlg.ShowModal() == wx.ID_OK:
            employee_name = dlg.GetValue()
            
            new_employee = {
                "name": employee_name,
                "position": "员工",
                "status": "在职"
            }
            
            if self.crud_manager.insert_data(new_employee):
                if hasattr(self.GetParent(), 'connection'):
                    self.GetParent().connection.commit()
                
                wx.MessageBox("员工添加成功", "成功", wx.OK | wx.ICON_INFORMATION)
                self.load_data_from_db()
            else:
                wx.MessageBox("添加员工失败，请重试", "错误", wx.OK | wx.ICON_ERROR)
        
        dlg.Destroy()
    
    def OnDeleteEmployee(self, event):
        """删除选中行"""
        selected_ids = self.get_selected_ids()
        if not selected_ids:
            wx.MessageBox("请先选择要删除的员工", "提示", wx.OK | wx.ICON_INFORMATION)
            return
        
        self.delete_employees(selected_ids)
    
    def delete_employees(self, employee_ids):
        """删除员工"""
        confirm = wx.MessageDialog(
            self, 
            f"确定要删除选中的 {len(employee_ids)} 名员工吗？",
            "确认删除",
            wx.YES_NO | wx.NO_DEFAULT | wx.ICON_WARNING
        )
        
        if confirm.ShowModal() != wx.ID_YES:
            confirm.Destroy()
            return
        
        if self.crud_manager.delete_data(employee_ids):
            if hasattr(self.GetParent(), 'connection'):
                self.GetParent().connection.commit()
            
            wx.MessageBox("员工删除成功", "成功", wx.OK | wx.ICON_INFORMATION)
            self.load_data_from_db()
        else:
            wx.MessageBox("删除员工失败，请重试", "错误", wx.OK | wx.ICON_ERROR)
        
        confirm.Destroy()
    
    def on_search_table(self, event):
        """搜索表格"""
        search_text = self.m_textCtrl42.GetValue().strip()
        if not search_text:
            self.load_data_from_db()
            return
        
        search_column_index = self.m_choice2.GetSelection()
        if search_column_index == wx.NOT_FOUND or search_column_index == 0:
            search_column = None
        else:
            search_column = self.m_choice2.GetString(search_column_index)
        
        search_results = self.crud_manager.search_data(search_column, search_text)
        self.m_dataViewListCtrl1.DeleteAllItems()
        
        for row in search_results:
            self.m_dataViewListCtrl1.AppendItem([False] + [str(value) if value is not None else "" for value in row])
        
        self.update_status()
    
    def cancel_selection(self, event):
        """取消选择"""
        # 清除所有复选框选择
        for row in range(self.m_dataViewListCtrl1.GetItemCount()):
            self.m_dataViewListCtrl1.SetToggleValue(row, 0, False)
        
        self.selected_rows.clear()
        self.update_status()
    
    def on_edit(self, event):
        """保存选中行的修改"""
        if not self.selected_rows:
            wx.MessageBox("请先选择要修改的行", "提示", wx.OK | wx.ICON_INFORMATION)
            return
        
        updated_count = 0
        error_count = 0
        
        for row in self.selected_rows:
            row_data = {}
            for col_index in range(1, self.m_dataViewListCtrl1.GetColumnCount()):
                col_name = self.m_dataViewListCtrl1.GetColumn(col_index).GetTitle()
                value = self.m_dataViewListCtrl1.GetTextValue(row, col_index)
                row_data[col_name] = value
            
            employee_id = self.m_dataViewListCtrl1.GetTextValue(row, 1)
            update_data = {k: v for k, v in row_data.items() if k != self.crud_manager.primary_key}
            
            if self.crud_manager.update_data(update_data, employee_id):
                updated_count += 1
            else:
                error_count += 1
        
        if hasattr(self.GetParent(), 'connection'):
            self.GetParent().connection.commit()
        
        message = f"成功更新 {updated_count} 条记录"
        if error_count > 0:
            message += f"，失败 {error_count} 条记录"
        wx.MessageBox(message, "保存结果", wx.OK | wx.ICON_INFORMATION)
        
        self.load_data_from_db()
    
    def load_data(self, event=None):
        """刷新数据"""
        self.load_data_from_db()
        wx.MessageBox("数据已刷新", "信息", wx.OK | wx.ICON_INFORMATION)