extends SceneTree

const GxReaderScript := preload("res://nova_assets/gx/gx_reader.gd")
const EVIDENCE := "res://evidence/gx_attachment_native_evidence_20260725.json"
const COMMON := "C:/Program Files (x86)/Nova1492/datan/common"


func _init() -> void:
	var evidence = JSON.parse_string(FileAccess.get_file_as_string(EVIDENCE))
	if not evidence is Dictionary:
		_finish_failure("evidence JSON")
		return
	var files := {}
	for filename in DirAccess.get_files_at(COMMON):
		files[filename.to_lower()] = filename
	var checked := 0
	for expected in evidence.corpus.assets:
		var key := str(expected.gx).to_lower()
		if not files.has(key):
			_finish_failure("missing " + key)
			return
		var path := COMMON.path_join(str(files[key]))
		if FileAccess.get_sha256(path).to_upper() != str(expected.gx_sha256):
			_finish_failure("hash " + path)
			return
		var actual: Dictionary = GxReaderScript.read_file(path)
		if not bool(actual.get("ok", false)):
			_finish_failure("parse " + path)
			return
		if actual.nodes.size() != expected.nodes.size():
			_finish_failure("node count " + path)
			return
		if actual.meshes.size() != int(expected.mesh_count):
			_finish_failure("mesh count " + path)
			return
		for index in range(actual.nodes.size()):
			var actual_node: Dictionary = actual.nodes[index]
			var expected_node: Dictionary = expected.nodes[index]
			if str(actual_node.name) != str(expected_node.name):
				_finish_failure(
					"node name %s:%d actual=%s expected=%s" % [
						path, index, str(actual_node.name), str(expected_node.name)
					]
				)
				return
			if int(actual_node.parent_index) != int(expected_node.parent_index):
				_finish_failure("node parent %s:%d" % [path, index])
				return
			if int(actual_node.flags) != str(expected_node.flags).hex_to_int():
				_finish_failure("node flags %s:%d" % [path, index])
				return
			var matrix: PackedFloat32Array = actual_node.matrix
			if matrix.size() != 16:
				_finish_failure("matrix size %s:%d" % [path, index])
				return
			for component in range(16):
				if not is_equal_approx(
					float(matrix[component]),
					float(expected_node.matrix[component])
				):
					_finish_failure(
						"matrix %s:%d:%d" % [path, index, component]
					)
					return
		checked += 1
	if checked != 217:
		_finish_failure("checked %d" % checked)
		return
	print("PART_GX_NATIVE_EVIDENCE_PARITY_OK 217/217")
	quit(0)


func _finish_failure(message: String) -> void:
	push_error("PART_GX_NATIVE_EVIDENCE_PARITY_FAILED " + message)
	quit(1)
