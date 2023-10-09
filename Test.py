import unreal

unreal.log("Hello World.Unreal")

# 创建一个新的MetaHumanCaptureSource
# 通过unreal.MetaHumanCaptureSourceFactoryNew()创建一个新的MetaHumanCaptureSource
# 通过unreal.AssetToolsHelpers.get_asset_tools()获取AssetTools
# 通过AssetTools.create_asset()创建一个新的MetaHumanCaptureSource
# 通过unreal.AssetImportTask()创建一个新的AssetImportTask
# 通过AssetImportTask.set_editor_property()设置属性
# 通过AssetTools.import_asset_tasks()导入AssetImportTask
# 通过unreal.AssetRegistryHelpers.get_asset_registry()获取AssetRegistry
# 通过AssetRegistry.get_asset_by_object_path()获取Asset
# 通过Asset.get_asset()获取AssetData
# 通过AssetData.get_asset()获取Asset
# 通过Asset.get_editor_property()获取属性
# 通过Asset.set_editor_property()设置属性
# 通过Asset.save_asset()保存Asset
# 通过unreal.EditorAssetLibrary.load_asset()加载Asset
# 通过unreal.EditorAssetLibrary.save_loaded_asset()保存Asset
# 通过unreal.EditorAssetLibrary.save_asset()保存Asset
# 通过unreal.EditorAssetLibrary.save_directory()保存Asset
# 通过unreal.EditorAssetLibrary.save_all_assets()保存Asset
# 通过unreal.EditorAssetLibrary.save_loaded_assets()保存Asset




# 通过unreal.AssetToolsHelpers.get_asset_tools()获取AssetTools
asset_tools = unreal.AssetToolsHelpers.get_asset_tools()


# # 创建一个FootageCaptureData
# footage_name = "Footage_CreateByPython"
# footage_package_path = "/Game/Footages"
# footage = asset_tools.create_asset(footage_name, footage_package_path, asset_class=unreal.FootageCaptureData, factory= unreal.FootageCaptureDataFactoryNew())

# # 创建ImgMediaSource
# #--------------------------

# ims_rgb_name = "IMS_RGB_CreateByPython"
# ims_depth_name = "IMS_Depth_CreateByPython"
# ims_package_path = "/Game/Python_Ingested"

# # 创建AssetImportTask
# ims_AssetImportTask = unreal.AssetImportTask()
# ims_AssetImportTask.set_editor_property("automated",True)
# ims_AssetImportTask.set_editor_property("replace_existing",True)
# ims_AssetImportTask.set_editor_property("save",True)

# # 创建ImgMediaSource
# ims_automatedData = unreal.AutomatedAssetImportData()
# ims_automatedData.set_editor_property("destination_path", "Game/Img")

# ims_factory = unreal.ImgMediaSourceFactoryNew()
# # img_factory.set_editor_property("automated_import_data", img_automatedData)
# ims_factory.set_editor_property("asset_import_task", ims_AssetImportTask)

# # 创建 FrameRate
# ims_frameRate = unreal.FrameRate()
# ims_frameRate.set_editor_property("denominator", 1)
# ims_frameRate.set_editor_property("numerator", 30)

# # 创建RGB MediaSource
# ims_rgb_sequencePath = "Content/Python_Ingested/Video_Frames"
# ims_rgb_MediaSource = asset_tools.create_asset(ims_rgb_name, ims_package_path, asset_class=unreal.ImgMediaSource, factory= unreal.ImgMediaSourceFactoryNew())
# ims_rgb_MediaSource.set_editor_property("sequence_path", unreal.DirectoryPath(ims_rgb_sequencePath))

# # 创建depth MediaSource
# ims_depth_sequencePath = "Content/Python_Ingested/Depth_Frames"
# ims_depth_MediaSource = asset_tools.create_asset(ims_depth_name, ims_package_path, asset_class=unreal.ImgMediaSource, factory= unreal.ImgMediaSourceFactoryNew())
# ims_depth_MediaSource.set_editor_property("sequence_path", unreal.DirectoryPath(ims_depth_sequencePath))

# #---------------------------

# # 创建Lens File
# #---------------------------

# # 创建RGB Lens
# lens_rgb_name = "Lens_RGB_CreateByPython"
# lens_package_path = "/Game/Python_Ingested"
# rgb_lens = asset_tools.create_asset(lens_rgb_name, lens_package_path, asset_class=unreal.LensFile, factory= unreal.LensFileFactoryNew())

# rgb_lensInfo = unreal.LensInfo()
# rgb_lensInfo.image_dimensions = unreal.IntPoint(720, 1280)

# rgb_lens.set_editor_property("lens_info", rgb_lensInfo)

# # 创建Depth Lens
# lens_depth_name = "Lens_Depth_CreateByPython"
# lens_package_path = "/Game/Python_Ingested"
# depth_lens = asset_tools.create_asset(lens_depth_name, lens_package_path, asset_class=unreal.LensFile, factory= unreal.LensFileFactoryNew())
# depth_lens.set_editor_property("lens_info", rgb_lensInfo)
# #---------------------------


# 创建一个新的MetaHumanCaptureSource
cs_name = "CS_CreateByPython"
cs_package_path = "/Game/CaptureSources"

# 删除目录
isExist = unreal.EditorAssetLibrary.does_asset_exist(cs_package_path + "/" + cs_name)
if isExist:
    unreal.EditorAssetLibrary.delete_asset(cs_package_path + "/" + cs_name)

mh_cs = asset_tools.create_asset(cs_name, cs_package_path, unreal.MetaHumanCaptureSource, unreal.MetaHumanCaptureSourceFactoryNew())
mh_cs.set_editor_property("capture_source_type", unreal.MetaHumanCaptureSourceType.LIVE_LINK_FACE_ARCHIVES)
mh_cs.set_editor_property("storage_path", ["F:/MyCode/UnrealEngine/LiveLinkFace_Slate/20230803_MySlate_14"])

# 创建一个新的MetaHumanIdentity
id_name =  "ID_CreateByPython"
id_package_path = "/Game/MHIdentity"
isExist = unreal.EditorAssetLibrary.does_asset_exist(id_package_path + "/" + id_name)
if isExist:
    unreal.EditorAssetLibrary.delete_asset(id_package_path + "/" + id_name)

mh_id = asset_tools.create_asset(id_name, id_package_path, asset_class=unreal.MetaHumanIdentity, factory= unreal.MetaHumanIdentityFactoryNew())


# # 添加一个MetaHumanIdentityFace
# part_face = mh_id.get_or_create_part_of_class(unreal.MetaHumanIdentityFace)
# # 添加一个MetaHumanIdentityPose
# print("part_face", part_face)
# # 创建一个MetaHumanIdentityPose
# pose_Neutral = unreal.MetaHumanIdentityPose()
# pose_Neutral.pose_type = unreal.IdentityPoseType.NEUTRAL

# part_face.add_pose_of_type(unreal.IdentityPoseType.NEUTRAL, pose_Neutral)


# 获取MetaHumanIdentityFace
# part_face = mh_id.find_part_of_class(unreal.MetaHumanIdentityFace)
# print("part_face", part_face)

# 获取MetaHumanIdentityPose
# pose_Neutral = part_face.find_pose_by_type(unreal.IdentityPoseType.NEUTRAL)
# print("pose_Neutral", pose_Neutral)

# unreal.EditorAssetLibrary

# 获取AssetEditorSubsystem
# asset_editor_subsystem = unreal.get_editor_subsystem(unreal.AssetEditorSubsystem)
# asset_editor_subsystem.open_editor_for_assets([mh_cs, mh_id])

# 通过资源编辑器打开资产,下面的方法已经废弃
# asset_tools.open_editor_for_assets([mh_cs, mh_id])




