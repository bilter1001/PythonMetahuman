import unreal 


unreal.log_error("Python 4 test")

captureSourcePath = "Game/PythonTest/CS_CreateByPython"
IDPath = "Game/PythonTest/ID_CreateByPython"
storage_path = r"D:\BaiduNetdiskDownload\20230803_MySlate_43"
spp =  ["(path=\"D:/BaiduNetdiskDownload/20230803_MySlate_43\")"]


cp = unreal.MetaHumanCaptureSourceFactoryNew()

# 替换为你的Sequencer资源的实际路径
#asset_path = "/Game/PythonTest/CS_Python.CS_Python"
# 加载关卡序列资源
#ss_asset = unreal.EditorAssetLibrary.load_asset(asset_path)

asset_tools = unreal.AssetToolsHelpers.get_asset_tools()

asset_name = "CS_CreateByPython"
package_path = "/Game/PythonTest"
my_cs = asset_tools.create_asset(asset_name, package_path, None, unreal.MetaHumanCaptureSourceFactoryNew())

my_cs.set_editor_property("capture_source_type", unreal.MetaHumanCaptureSourceType.LIVE_LINK_FACE_ARCHIVES)
my_cs.set_editor_property("storage_path", ["D:/BaiduNetdiskDownload/20230803_MySlate_43"])
#my_cs.set_editor_property("startup",unreal.TakeIngestMode.ASYNC)

taskN = my_cs.set_target_path("Game/PythonTest/", captureSourcePath)
print(taskN)

my_cs.startup(unreal.TakeIngestMode.ASYNC)


id_name =  "ID_CreateByPython"
my_id = asset_tools.create_asset(id_name, package_path, asset_class=unreal.MetaHumanIdentity, factory= unreal.MetaHumanIdentityFactoryNew())





#unreal.SystemLibrary.execute_console_command(unreal.EditorLevelLibrary.get_editor_world(), "Open Edit/Plugins")

#menus = unreal.ToolMenus.get()
main_editor_window =  unreal.ToolMenus.get()
cm_menu = main_editor_window.find_menu("LevelEditor.MainMenu.Tools.Capture Manager")
if not cm_menu:
        print("Failed to find the 'cm_menu' menu. Something is wrong in the force!")

# 因为import_asset_tasks需要的参数是数组Array
# 所以我们先把import_tasks设成list



file = unreal.AssetImportTask()
# 按照属性描述，设置属性
file.set_editor_property("automated",True)# 是否避免弹框对话
#file.set_editor_property("destination_name","ABC")# 资产重命名，若空字符串则为文件原名
#file.set_editor_property("destination_path","/Game/texture/")# 资产存放路径，支持新建文件夹（比如Game里面没有texture的，它会帮你建一个名为texture的文件夹）
file.set_editor_property("filename",captureSourcePath)# 从哪里导入文件
file.set_editor_property("replace_existing",True)# 是否覆盖现在资产
file.set_editor_property("replace_existing_settings",True)# 覆盖时是否替换现在设置
file.set_editor_property("save",True)# 导入后是否保存


#unreal.AssetToolsHelpers.get_asset_tools().import_asset_tasks(file)
#my_fc.set_editor_property("asset_import_task", file)




# unreal.EditorUtilitySubsystem().spawn_and_register_tab(unreal.EditorAssetLibrary.load_asset("/path_to_your_widget"))
#unreal.SystemLibrary.execute_console_command(unreal.EditorLevelLibrary.get_editor_world(), "Open CaptureManager")


# unreal.EditorUtilitySubsystem().register_and_execute_task("LevelEditor.MainMenu/Tools/Capture Manager")

# 如果你需要执行某个菜单项的操作，可以使用以下方法：
# unreal.EditorUtilitySubsystem().execute_tool("YourRegisteredToolName")    

# 如果你需要执行某个菜单项的操作，可以使用以下方法：
#unreal.EditorUtilitySubsystem().execute_tool("YourRegisteredToolName")


# factory = unreal.BlueprintFactory()
# factory.set_editor_property("ParentClass", unreal.Actor)
# asset_tools = unreal.AssetToolsHelpers.get_asset_tools()