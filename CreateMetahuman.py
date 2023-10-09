import unreal
import os





if __name__ == '__main__':
    
    unreal.log("Hello World.Unreal")

    asset_tools = unreal.AssetToolsHelpers.get_asset_tools()


    # 删除MyAnimator
    animator_root_path = "/Game/MyAnimator"    
    isDirExist = unreal.EditorAssetLibrary.does_directory_exist(animator_root_path)
    if isDirExist:
        unreal.EditorAssetLibrary.delete_directory(animator_root_path)
        print("MyAnimator文件夹unreal删除成功")

    # 删除目录和文件
    project_animator_path = "E:/Unreal Projects/PythonMetahuman/Content/MyAnimator"
    if os.path.exists(project_animator_path) and os.path.isdir(project_animator_path):
        # 删除目录和文件
        for root, dirs, files in os.walk(project_animator_path, topdown=False):
            for name in files:
                os.remove(os.path.join(root, name))                
            for name in dirs:
                os.rmdir(os.path.join(root, name))                
        print(project_animator_path,"文件夹和文件删除成功")
    else:
        print(project_animator_path,"文件夹不存在或路径不是文件夹")


    # 创建一个新的MetaHumanCaptureSource
    cs_name = "MyCS"
    cs_package_path = "/Game/MyAnimator"

    isExist = unreal.EditorAssetLibrary.does_asset_exist(cs_package_path + "/" + cs_name)
    if isExist:
        unreal.EditorAssetLibrary.delete_asset(cs_package_path + "/" + cs_name)

    mh_cs = asset_tools.create_asset(cs_name, cs_package_path, unreal.MetaHumanCaptureSource, unreal.MetaHumanCaptureSourceFactoryNew())
    mh_cs.set_editor_property("capture_source_type", unreal.MetaHumanCaptureSourceType.LIVE_LINK_FACE_ARCHIVES)
    mh_cs.set_editor_property("storage_path", ["F:/MyCode/UnrealEngine/LiveLinkFace_Slate/20230803_MySlate_14"])

    # 创建一个新的MetaHumanIdentity
    id_name =  "MyMI"
    id_package_path = "/Game/MyAnimator"
    isExist = unreal.EditorAssetLibrary.does_asset_exist(id_package_path + "/" + id_name)
    if isExist:
        unreal.EditorAssetLibrary.delete_asset(id_package_path + "/" + id_name)

    mh_id = asset_tools.create_asset(id_name, id_package_path, asset_class=unreal.MetaHumanIdentity, factory= unreal.MetaHumanIdentityFactoryNew())

    unreal.EditorAssetLibrary.save_directory(animator_root_path)