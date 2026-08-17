extends SceneTree

const GxReaderScript := preload("res://nova_assets/gx/gx_reader.gd")
const XfiReaderScript := preload("res://nova_assets/xfi/xfi_reader.gd")

const CASES := [
	{
		"paths": [
			"C:/Program Files (x86)/Nova1492/datan/common/legs24_sts.gx",
			"C:/Program Files (x86)/Nova1492/datan/common/n_body44_brps.gx",
			"C:/Program Files (x86)/Nova1492/datan/common/arm76_orns.gx",
		],
		"mesh_counts": [16, 8, 25],
		"bp_origin": Vector3(0.0000000048820614, 1.5102072746, 0.0),
		"ap_origin": Vector3(-0.0015319951, 1.8444242746, 0.483486),
	},
	{
		"paths": [
			"C:/Program Files (x86)/Nova1492/datan/common/legs50_pps.gx",
			"C:/Program Files (x86)/Nova1492/datan/common/body20_prsd.gx",
			"C:/Program Files (x86)/Nova1492/datan/common/arm81_rtro.GX",
		],
		"mesh_counts": [25, 3, 15],
		"bp_origin": Vector3(0.0, 1.6011675596, 0.0),
		"ap_origin": Vector3(-0.000008, 1.8658175596, 0.000472),
	},
]


func _initialize() -> void:
	var failures: Array[String] = []
	for fixture in CASES:
		var paths: Array = fixture.paths
		var parsed := [
			GxReaderScript.read_file(paths[0]),
			GxReaderScript.read_file(paths[1]),
			GxReaderScript.read_file(paths[2]),
		]
		for index in range(3):
			if not parsed[index].get("ok", false):
				failures.append("parse failed: %s" % paths[index])
			elif parsed[index].meshes.size() != fixture.mesh_counts[index]:
				failures.append(
					"mesh count %s: got %d expected %d" % [
						paths[index].get_file(),
						parsed[index].meshes.size(),
						fixture.mesh_counts[index],
					]
				)
		var mp_root := _first_mesh_transform(parsed[0])
		var bp_root := _first_mesh_transform(parsed[1])
		var mp_sockets: Array = XfiReaderScript.read_for_gx(paths[0]).transforms
		var bp_sockets: Array = XfiReaderScript.read_for_gx(paths[1]).transforms
		if mp_sockets.size() < 1 or bp_sockets.size() < 3:
			failures.append("missing XFI sockets: %s" % paths[0].get_file())
			continue
		var bp_part: Transform3D = mp_root * mp_sockets[0]
		var ap_part: Transform3D = bp_part * bp_root * bp_sockets[2]
		if not bp_part.origin.is_equal_approx(fixture.bp_origin):
			failures.append(
				"BP origin %s: got %s expected %s" % [
					paths[0].get_file(), bp_part.origin, fixture.bp_origin
				]
			)
		if not ap_part.origin.is_equal_approx(fixture.ap_origin):
			failures.append(
				"AP origin %s: got %s expected %s" % [
					paths[0].get_file(), ap_part.origin, fixture.ap_origin
				]
			)
	if failures.is_empty():
		print("REFERENCE_ASSEMBLY_CONTRACT_OK 2/2")
		quit(0)
	else:
		for failure in failures:
			push_error(failure)
		quit(1)


func _first_mesh_transform(parsed: Dictionary) -> Transform3D:
	if parsed.meshes.is_empty():
		return Transform3D.IDENTITY
	return _world_transform(parsed.nodes, int(parsed.meshes[0].node_index))


func _world_transform(nodes: Array, node_index: int) -> Transform3D:
	var result := Transform3D.IDENTITY
	var chain: Array[int] = []
	var visited := {}
	while node_index >= 0 and node_index < nodes.size() and not visited.has(node_index):
		visited[node_index] = true
		chain.push_front(node_index)
		node_index = int(nodes[node_index].parent_index)
	for index in chain:
		var local_transform: Transform3D
		if nodes[index].has("animation"):
			local_transform = GxReaderScript.animation_transform(
				nodes[index].animation, 0
			)
		else:
			local_transform = GxReaderScript.node_transform(nodes[index])
		result = result * local_transform
	return result
