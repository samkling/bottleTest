from bottle import run, route

@route('/data')
def data():
	jsonStr = '''
{
	"subs": [{
			"src": "asalimi",
			"ts": {
				"$date": 1517942226516
			},
			"fname": "84707.exe"
		}, {
			"src": "asalimi",
			"ts": {
				"$date": 1517942206996
			},
			"fname": "84707.exe"
		}
	],
	"update-ts": {
		"$date": 1517942201341
	},
	"meta": {
		"ImportHash": "2f12f2bc4e240b2aa4b765273d37e4e215f35b55",
		"Imports": [{
				"imports": ["IsPwrSuspendAllowed"],
				"dllname": "POWRPROF.dll"
			}, {
				"imports": ["FlsFree", "GetACP", "GetOverlappedResult", "GetConsoleCP", "LocalUnlock", "GetModuleHandleA", "GetModuleFileNameA", "GetBinaryTypeA", "WaitForSingleObjectEx", "FreeConsole", "GetExitCodeThread", "OpenFile", "CreateTimerQueue", "RaiseException", "GetLastError", "InterlockedExchange", "FreeLibrary", "GetProcAddress", "LocalFree", "LocalAlloc", "LoadLibraryA", "HeapFree"],
				"dllname": "KERNEL32.dll"
			}, {
				"imports": ["LPtoDP", "CloseEnhMetaFile", "GetAspectRatioFilterEx", "AddFontResourceW"],
				"dllname": "GDI32.dll"
			}, {
				"imports": ["SetupQuerySourceListW"],
				"dllname": "SETUPAPI.dll"
			}, {
				"imports": [],
				"dllname": "msi.dll"
			}, {
				"imports": ["SystemTimeToVariantTime"],
				"dllname": "OLEAUT32.dll"
			}, {
				"imports": ["RegOpenUserClassesRoot"],
				"dllname": "ADVAPI32.dll"
			}, {
				"imports": ["SHAutoComplete", "StrChrIW"],
				"dllname": "SHLWAPI.dll"
			}
		],
		"PEHeader": {
			"subsystem": 2,
			"OSVersion": "5.0",
			"imageSize": 147456,
			"LinkerVersion": "0.4",
			"EntryPoint": 9088,
			"Subsystemversion": "5.0",
			"peChksum": 0,
			"ImageVersion": "0.0",
			"BaseAddress": 4194304,
			"creationDate": {
				"$date": 1517971154000
			},
			"arch": 332,
			"imageType": 258
		},
		"SummaryInfo": {},
		"Debug": {
			"pdb": "BBSsssEEE.pdb"
		},
		"ImportHashVTCompatable": "69a4c573609bcfae240867d0afc9aa41",
		"Sections": [{
				"characteristics": 1610616864,
				"rawSize": 126976,
				"offset": 4096,
				"name": ".text\u0000\u0000\u0000",
				"size": 125332
			}, {
				"characteristics": 3221225536,
				"rawSize": 4096,
				"offset": 131072,
				"name": ".data\u0000\u0000\u0000",
				"size": 4688
			}, {
				"characteristics": 1073741888,
				"rawSize": 4096,
				"offset": 139264,
				"name": ".idata\u0000\u0000",
				"size": 1158
			}, {
				"characteristics": 1107296320,
				"rawSize": 4096,
				"offset": 143360,
				"name": "DATA\u0000\u0000\u0000\u0000",
				"size": 508
			}
		]
	},
	"entropy": 6.3233354203925485,
	"detections_die": [{
			"extras": ["EXE32"],
			"type": "linker",
			"class": "PE",
			"version": "0.4",
			"software": "unknown"
		}
	],
	"size": 143360,
	"importts": {
		"$date": 1517942226522
	},
	"module_stats": [{
			"rt": 0.056999,
			"name": "yara processor",
			"st": "P"
		}, {
			"rt": 0.331946,
			"name": "detect-it-easy processor",
			"st": "P"
		}, {
			"rt": 0.00105,
			"name": "libmagic processor",
			"st": "P"
		}, {
			"rt": 0.125804,
			"name": "pe processor",
			"st": "P"
		}, {
			"rt": 0.00143,
			"name": "md5_collision_detection",
			"st": "P"
		}
	],
	"sha256": "01486a0b61e7956d876508d0683c818b39372bd2f55311e92490a0bfddc3f845",
	"type": "PE32 executable for MS Windows (GUI) Intel 80386 32-bit",
	"public": true,
	"status": {
		"yara": "COMP",
		"meta": "COMP"
	},
	"relationships": [],
	"file_class": "PECOFF",
	"metrics": {
		"yara_update": 1.9e-05,
		"total": 0.628864,
		"total_module": 0.523098,
		"file": 0.1051
	},
	"fuzzy": {
		"sig1": "cPBCWr0CE+mb/v/ADN5CGFGJuWenTIr/0H3Uefg6wwbYIwTHGYbRiLqBC8nWfpA",
		"full": "1536:cPBCWr0CE+mb/v/ADN5CGFGJuWenTIr/0H3Uefg6wwbYIwTHGYbRiLqBC8nWfpA:c/Ez7Ap5CyGspnT80HJTww16HGUiLxA",
		"sig2": "c/Ez7Ap5CyGspnT80HJTww16HGUiLxA",
		"bSize1": 1536,
		"bSize2": 3072,
		"odds2": 15,
		"odds1": 32
	},
	"md5": "85be259d134271cfa09d46e61d0f0b9e",
	"sha1": "a6b5215fdbe5a4da0237bab551153f2b8c0a6434",
	"sha512": "ef0ad953d1e722dfac1c94e73dbd1fcf4e9807e3902aa6906ae1c0725b82135152041e5834ba9299ebc503f6fd26e83576a0cf801e438b7acd54d13b71de3204",
	"disk_location": "s3://zaim-samples/01/48/2018-02-06/01486a0b61e7956d876508d0683c818b39372bd2f55311e92490a0bfddc3f845.lzma.aes-256-cbc.2016-11-02",
	"sha384": "38640e9b9e9fdc6ccdfa2c94d743af7f432bf457bbad5b57c09a99ad576ae13eb93bba063edd4b9fcadb55f16505a306",
	"_id": "a6b5215fdbe5a4da0237bab551153f2b8c0a6434"
}
	'''

	return jsonStr

if __name__ == '__main__':
	run()