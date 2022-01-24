## Hard crashes
graphics froze, unable to switch to alternate session. required system reboot.

### 1 

<details><summary>kern.log</summary>
```
Jan 23 22:04:07 tiana kernel: [ 3053.894639] perf: interrupt took too long (2526 > 2500), lowering kernel.perf_event_max_sample_rate to 79000
Jan 23 22:04:25 tiana kernel: [ 3072.743608] [drm:amdgpu_vm_handle_fault [amdgpu]] *ERROR* Can't handle page fault (-12)
Jan 23 22:04:25 tiana kernel: [ 3072.743617] gmc_v9_0_process_interrupt: 3 callbacks suppressed
Jan 23 22:04:25 tiana kernel: [ 3072.743620] amdgpu 0000:2b:00.0: amdgpu: [mmhub0] retry page fault (src_id:0 ring:0 vmid:8 pasid:32779, for process python pid 39593 thread python pid 39593)
Jan 23 22:04:25 tiana kernel: [ 3072.743621] amdgpu 0000:2b:00.0: amdgpu:   in page starting at address 0x0000000080000000 from client 18
Jan 23 22:04:25 tiana kernel: [ 3072.743622] amdgpu 0000:2b:00.0: amdgpu: VM_L2_PROTECTION_FAULT_STATUS:0x00840051
Jan 23 22:04:25 tiana kernel: [ 3072.743624] amdgpu 0000:2b:00.0: amdgpu:        Faulty UTCL2 client ID: MP0 (0x0)
Jan 23 22:04:25 tiana kernel: [ 3072.743624] amdgpu 0000:2b:00.0: amdgpu:        MORE_FAULTS: 0x1
Jan 23 22:04:25 tiana kernel: [ 3072.743625] amdgpu 0000:2b:00.0: amdgpu:        WALKER_ERROR: 0x0
Jan 23 22:04:25 tiana kernel: [ 3072.743626] amdgpu 0000:2b:00.0: amdgpu:        PERMISSION_FAULTS: 0x5
Jan 23 22:04:25 tiana kernel: [ 3072.743627] amdgpu 0000:2b:00.0: amdgpu:        MAPPING_ERROR: 0x0
Jan 23 22:04:25 tiana kernel: [ 3072.743627] amdgpu 0000:2b:00.0: amdgpu:        RW: 0x1
Jan 23 22:04:34 tiana kernel: [ 3081.747295] qcm fence wait loop timeout expired
Jan 23 22:04:34 tiana kernel: [ 3081.747298] The cp might be in an unrecoverable state due to an unsuccessful queues preemption
Jan 23 22:04:34 tiana kernel: [ 3081.747300] amdgpu: Failed to evict process queues
Jan 23 22:04:34 tiana kernel: [ 3081.747301] amdgpu: Failed to evict queues of pasid 0x800b
Jan 23 22:04:34 tiana kernel: [ 3081.747745] amdgpu 0000:2b:00.0: amdgpu: GPU reset begin!
Jan 23 22:04:35 tiana kernel: [ 3081.971320] [drm] psp command (0x2) failed and response status is (0x117)
Jan 23 22:04:35 tiana kernel: [ 3081.971322] [drm] free PSP TMR buffer
Jan 23 22:04:35 tiana kernel: [ 3082.004232] amdgpu 0000:2b:00.0: amdgpu: BACO reset
Jan 23 22:04:35 tiana kernel: [ 3082.557394] amdgpu 0000:2b:00.0: amdgpu: GPU reset succeeded, trying to resume
Jan 23 22:04:35 tiana kernel: [ 3082.557567] [drm] PCIE GART of 512M enabled (table at 0x000000F400900000).
Jan 23 22:04:35 tiana kernel: [ 3082.557589] [drm] VRAM is lost due to GPU reset!
Jan 23 22:04:35 tiana kernel: [ 3082.557788] [drm] PSP is resuming...
Jan 23 22:04:35 tiana kernel: [ 3082.744844] [drm] reserve 0x400000 from 0xf7fec00000 for PSP TMR
Jan 23 22:04:35 tiana kernel: [ 3082.763540] ------------[ cut here ]------------
Jan 23 22:04:35 tiana kernel: [ 3082.763544] kernel BUG at drivers/gpu/drm/amd/amdgpu/amdgpu_vm.c:418!
Jan 23 22:04:35 tiana kernel: [ 3082.763553] invalid opcode: 0000 [#1] SMP NOPTI
Jan 23 22:04:35 tiana kernel: [ 3082.763557] CPU: 8 PID: 6094 Comm: kworker/8:0 Not tainted 5.10.0-11-amd64 #1 Debian 5.10.92-1
Jan 23 22:04:35 tiana kernel: [ 3082.763559] Hardware name: Micro-Star International Co., Ltd. MS-7A38/B450M PRO-VDH MAX (MS-7A38), BIOS B.B1 12/09/2020
Jan 23 22:04:35 tiana kernel: [ 3082.763564] Workqueue: events delayed_fput
Jan 23 22:04:35 tiana kernel: [ 3082.763658] RIP: 0010:amdgpu_vm_pt_descendant+0xa9/0xb0 [amdgpu]
Jan 23 22:04:35 tiana kernel: [ 3082.763660] Code: 53 00 00 ba 01 00 00 00 d3 e2 83 ea 01 31 c9 eb bd ba ff ff ff ff 83 f8 02 76 a2 83 f8 03 74 ed b9 ff ff ff ff eb a7 31 c0 c3 <0f> 0b 0f 1f 44 00 00 0f 1f 44 00 00 41 55 31 c0 41 89 cd b9 06 00
Jan 23 22:04:35 tiana kernel: [ 3082.763662] RSP: 0018:ffffa5528444fca8 EFLAGS: 00010246
Jan 23 22:04:35 tiana kernel: [ 3082.763664] RAX: 0000000000000001 RBX: ffffa5528444fcc8 RCX: ffff950f7a280000
Jan 23 22:04:35 tiana kernel: [ 3082.763666] RDX: 0000000000080000 RSI: ffffa5528444fcc8 RDI: ffff9515266b0070
Jan 23 22:04:35 tiana kernel: [ 3082.763667] RBP: ffff950f7a280000 R08: 0000000000000012 R09: ffff950fec9c0000
Jan 23 22:04:35 tiana kernel: [ 3082.763668] R10: 0000000000000009 R11: 0000000000000000 R12: 0000000000000000
Jan 23 22:04:35 tiana kernel: [ 3082.763669] R13: dead000000000122 R14: dead000000000100 R15: ffff950f8932b088
Jan 23 22:04:35 tiana kernel: [ 3082.763671] FS:  0000000000000000(0000) GS:ffff95164ec00000(0000) knlGS:0000000000000000
Jan 23 22:04:35 tiana kernel: [ 3082.763673] CS:  0010 DS: 0000 ES: 0000 CR0: 0000000080050033
Jan 23 22:04:35 tiana kernel: [ 3082.763674] CR2: 00007f553cfd48e0 CR3: 000000015013e000 CR4: 0000000000350ee0
Jan 23 22:04:35 tiana kernel: [ 3082.763676] Call Trace:
Jan 23 22:04:35 tiana kernel: [ 3082.763762]  amdgpu_vm_pt_next_dfs+0x2f/0x80 [amdgpu]
Jan 23 22:04:35 tiana kernel: [ 3082.763847]  amdgpu_vm_free_pts+0x117/0x200 [amdgpu]
Jan 23 22:04:35 tiana kernel: [ 3082.763930]  amdgpu_vm_fini+0x268/0x500 [amdgpu]
Jan 23 22:04:35 tiana kernel: [ 3082.764010]  amdgpu_driver_postclose_kms+0x155/0x220 [amdgpu]
Jan 23 22:04:35 tiana kernel: [ 3082.764027]  drm_file_free.part.0+0x21e/0x2a0 [drm]
Jan 23 22:04:35 tiana kernel: [ 3082.764042]  drm_release+0x65/0x110 [drm]
Jan 23 22:04:35 tiana kernel: [ 3082.764044]  __fput+0x95/0x240
Jan 23 22:04:35 tiana kernel: [ 3082.764046]  delayed_fput+0x1f/0x30
Jan 23 22:04:35 tiana kernel: [ 3082.764050]  process_one_work+0x1b6/0x350
Jan 23 22:04:35 tiana kernel: [ 3082.764052]  worker_thread+0x53/0x3e0
Jan 23 22:04:35 tiana kernel: [ 3082.764054]  ? process_one_work+0x350/0x350
Jan 23 22:04:35 tiana kernel: [ 3082.764057]  kthread+0x11b/0x140
Jan 23 22:04:35 tiana kernel: [ 3082.764059]  ? __kthread_bind_mask+0x60/0x60
Jan 23 22:04:35 tiana kernel: [ 3082.764062]  ret_from_fork+0x22/0x30
Jan 23 22:04:35 tiana kernel: [ 3082.764064] Modules linked in: bnep 8021q garp stp mrp llc snd_usb_audio snd_usbmidi_lib snd_rawmidi snd_seq_device iptable_nat nf_nat nf_conntrack nf_defrag_ipv6 nf_defrag_ipv4 libcrc32c iptable_mangle iptable_filter bluetooth jitterentropy_rng drbg ansi_cprng ecdh_generic rfkill ecc binfmt_misc edac_mce_amd snd_hda_codec_realtek kvm_amd snd_hda_codec_generic ppdev ledtrig_audio kvm irqbypass snd_hda_codec_hdmi ghash_clmulni_intel snd_hda_intel snd_intel_dspcfg soundwire_intel soundwire_generic_allocation snd_soc_core aesni_intel nls_ascii gspca_ov534 gspca_main nls_cp437 snd_compress videobuf2_vmalloc libaes soundwire_cadence videobuf2_memops crypto_simd videobuf2_v4l2 cryptd vfat glue_helper fat videobuf2_common snd_hda_codec videodev rapl snd_hda_core mc snd_hwdep soundwire_bus wmi_bmof efi_pstore pcspkr snd_pcm k10temp joydev snd_timer sp5100_tco watchdog snd ccp soundcore rng_core sg parport_pc parport evdev acpi_cpufreq fuse configfs efivarfs ip_tables x_tables autofs4 ext4 crc16
Jan 23 22:04:35 tiana kernel: [ 3082.764108]  mbcache jbd2 crc32c_generic sd_mod hid_generic usbhid hid amdgpu gpu_sched i2c_algo_bit ttm drm_kms_helper ahci xhci_pci libahci cec xhci_hcd libata drm r8169 nvme usbcore realtek mdio_devres scsi_mod crc32_pclmul nvme_core libphy crc32c_intel i2c_piix4 t10_pi crc_t10dif crct10dif_generic usb_common crct10dif_pclmul wmi crct10dif_common gpio_amdpt gpio_generic button
Jan 23 22:04:35 tiana kernel: [ 3082.764132] ---[ end trace 18e2c8457bb2c8c6 ]---
Jan 23 22:04:36 tiana kernel: [ 3082.928860] RIP: 0010:amdgpu_vm_pt_descendant+0xa9/0xb0 [amdgpu]
Jan 23 22:04:36 tiana kernel: [ 3082.928862] Code: 53 00 00 ba 01 00 00 00 d3 e2 83 ea 01 31 c9 eb bd ba ff ff ff ff 83 f8 02 76 a2 83 f8 03 74 ed b9 ff ff ff ff eb a7 31 c0 c3 <0f> 0b 0f 1f 44 00 00 0f 1f 44 00 00 41 55 31 c0 41 89 cd b9 06 00
Jan 23 22:04:36 tiana kernel: [ 3082.928863] RSP: 0018:ffffa5528444fca8 EFLAGS: 00010246
Jan 23 22:04:36 tiana kernel: [ 3082.928864] RAX: 0000000000000001 RBX: ffffa5528444fcc8 RCX: ffff950f7a280000
Jan 23 22:04:36 tiana kernel: [ 3082.928865] RDX: 0000000000080000 RSI: ffffa5528444fcc8 RDI: ffff9515266b0070
Jan 23 22:04:36 tiana kernel: [ 3082.928865] RBP: ffff950f7a280000 R08: 0000000000000012 R09: ffff950fec9c0000
Jan 23 22:04:36 tiana kernel: [ 3082.928866] R10: 0000000000000009 R11: 0000000000000000 R12: 0000000000000000
Jan 23 22:04:36 tiana kernel: [ 3082.928867] R13: dead000000000122 R14: dead000000000100 R15: ffff950f8932b088
Jan 23 22:04:36 tiana kernel: [ 3082.928868] FS:  0000000000000000(0000) GS:ffff95164ec00000(0000) knlGS:0000000000000000
Jan 23 22:04:36 tiana kernel: [ 3082.928868] CS:  0010 DS: 0000 ES: 0000 CR0: 0000000080050033
Jan 23 22:04:36 tiana kernel: [ 3082.928869] CR2: 00007f553cfd48e0 CR3: 000000015013e000 CR4: 0000000000350ee0
Jan 23 22:04:36 tiana kernel: [ 3083.008941] [drm] kiq ring mec 2 pipe 1 q 0
Jan 23 22:04:36 tiana kernel: [ 3083.120937] [drm] UVD and UVD ENC initialized successfully.
Jan 23 22:04:36 tiana kernel: [ 3083.220709] [drm] VCE initialized successfully.
Jan 23 22:04:36 tiana kernel: [ 3083.220729] amdgpu 0000:2b:00.0: amdgpu: ring gfx uses VM inv eng 0 on hub 0
Jan 23 22:04:36 tiana kernel: [ 3083.220730] amdgpu 0000:2b:00.0: amdgpu: ring comp_1.0.0 uses VM inv eng 1 on hub 0
Jan 23 22:04:36 tiana kernel: [ 3083.220731] amdgpu 0000:2b:00.0: amdgpu: ring comp_1.1.0 uses VM inv eng 4 on hub 0
Jan 23 22:04:36 tiana kernel: [ 3083.220732] amdgpu 0000:2b:00.0: amdgpu: ring comp_1.2.0 uses VM inv eng 5 on hub 0
Jan 23 22:04:36 tiana kernel: [ 3083.220733] amdgpu 0000:2b:00.0: amdgpu: ring comp_1.3.0 uses VM inv eng 6 on hub 0
Jan 23 22:04:36 tiana kernel: [ 3083.220734] amdgpu 0000:2b:00.0: amdgpu: ring comp_1.0.1 uses VM inv eng 7 on hub 0
Jan 23 22:04:36 tiana kernel: [ 3083.220735] amdgpu 0000:2b:00.0: amdgpu: ring comp_1.1.1 uses VM inv eng 8 on hub 0
Jan 23 22:04:36 tiana kernel: [ 3083.220736] amdgpu 0000:2b:00.0: amdgpu: ring comp_1.2.1 uses VM inv eng 9 on hub 0
Jan 23 22:04:36 tiana kernel: [ 3083.220737] amdgpu 0000:2b:00.0: amdgpu: ring comp_1.3.1 uses VM inv eng 10 on hub 0
Jan 23 22:04:36 tiana kernel: [ 3083.220738] amdgpu 0000:2b:00.0: amdgpu: ring kiq_2.1.0 uses VM inv eng 11 on hub 0
Jan 23 22:04:36 tiana kernel: [ 3083.220739] amdgpu 0000:2b:00.0: amdgpu: ring sdma0 uses VM inv eng 0 on hub 1
Jan 23 22:04:36 tiana kernel: [ 3083.220740] amdgpu 0000:2b:00.0: amdgpu: ring page0 uses VM inv eng 1 on hub 1
Jan 23 22:04:36 tiana kernel: [ 3083.220741] amdgpu 0000:2b:00.0: amdgpu: ring sdma1 uses VM inv eng 4 on hub 1
Jan 23 22:04:36 tiana kernel: [ 3083.220742] amdgpu 0000:2b:00.0: amdgpu: ring page1 uses VM inv eng 5 on hub 1
Jan 23 22:04:36 tiana kernel: [ 3083.220742] amdgpu 0000:2b:00.0: amdgpu: ring uvd_0 uses VM inv eng 6 on hub 1
Jan 23 22:04:36 tiana kernel: [ 3083.220743] amdgpu 0000:2b:00.0: amdgpu: ring uvd_enc_0.0 uses VM inv eng 7 on hub 1
Jan 23 22:04:36 tiana kernel: [ 3083.220744] amdgpu 0000:2b:00.0: amdgpu: ring uvd_enc_0.1 uses VM inv eng 8 on hub 1
Jan 23 22:04:36 tiana kernel: [ 3083.220745] amdgpu 0000:2b:00.0: amdgpu: ring vce0 uses VM inv eng 9 on hub 1
Jan 23 22:04:36 tiana kernel: [ 3083.220746] amdgpu 0000:2b:00.0: amdgpu: ring vce1 uses VM inv eng 10 on hub 1
Jan 23 22:04:36 tiana kernel: [ 3083.220747] amdgpu 0000:2b:00.0: amdgpu: ring vce2 uses VM inv eng 11 on hub 1
Jan 23 22:04:36 tiana kernel: [ 3083.222488] amdgpu 0000:2b:00.0: amdgpu: recover vram bo from shadow start
Jan 23 22:04:36 tiana kernel: [ 3083.223082] amdgpu 0000:2b:00.0: amdgpu: recover vram bo from shadow done
Jan 23 22:04:36 tiana kernel: [ 3083.223091] amdgpu 0000:2b:00.0: amdgpu: GPU reset(1) succeeded!
Jan 23 22:04:36 tiana kernel: [ 3083.223438] [drm] Skip scheduling IBs!
Jan 23 22:04:36 tiana kernel: [ 3083.223446] [drm] Skip scheduling IBs!
Jan 23 22:04:36 tiana kernel: [ 3083.223449] [drm] Skip scheduling IBs!
Jan 23 22:04:36 tiana kernel: [ 3083.223452] [drm] Skip scheduling IBs!
Jan 23 22:04:36 tiana kernel: [ 3083.223455] [drm] Skip scheduling IBs!
Jan 23 22:04:36 tiana kernel: [ 3083.223458] [drm] Skip scheduling IBs!
Jan 23 22:04:36 tiana kernel: [ 3083.223461] [drm] Skip scheduling IBs!
Jan 23 22:04:36 tiana kernel: [ 3083.223464] [drm] Skip scheduling IBs!
Jan 23 22:04:36 tiana kernel: [ 3083.223467] [drm] Skip scheduling IBs!
Jan 23 22:04:36 tiana kernel: [ 3083.223470] [drm] Skip scheduling IBs!
Jan 23 22:04:36 tiana kernel: [ 3083.223472] [drm] Skip scheduling IBs!
Jan 23 22:04:36 tiana kernel: [ 3083.223475] [drm] Skip scheduling IBs!
Jan 23 22:04:36 tiana kernel: [ 3083.223478] [drm] Skip scheduling IBs!
Jan 23 22:04:36 tiana kernel: [ 3083.223483] [drm] Skip scheduling IBs!
Jan 23 22:04:36 tiana kernel: [ 3083.223487] [drm] Skip scheduling IBs!
Jan 23 22:04:36 tiana kernel: [ 3083.223490] [drm] Skip scheduling IBs!
Jan 23 22:04:36 tiana kernel: [ 3083.223493] [drm] Skip scheduling IBs!
Jan 23 22:04:36 tiana kernel: [ 3083.223496] [drm] Skip scheduling IBs!
Jan 23 22:04:36 tiana kernel: [ 3083.223499] [drm] Skip scheduling IBs!
Jan 23 22:04:36 tiana kernel: [ 3083.223513] [drm] Skip scheduling IBs!
Jan 23 22:04:36 tiana kernel: [ 3083.223518] [drm] Skip scheduling IBs!
Jan 23 22:04:36 tiana kernel: [ 3083.223523] [drm] Skip scheduling IBs!
Jan 23 22:04:36 tiana kernel: [ 3083.223528] [drm] Skip scheduling IBs!
Jan 23 22:04:36 tiana kernel: [ 3083.223533] [drm] Skip scheduling IBs!
Jan 23 22:04:36 tiana kernel: [ 3083.223536] [drm] Skip scheduling IBs!
Jan 23 22:04:36 tiana kernel: [ 3083.223539] [drm] Skip scheduling IBs!
Jan 23 22:04:36 tiana kernel: [ 3083.223541] [drm] Skip scheduling IBs!
Jan 23 22:04:36 tiana kernel: [ 3083.223543] [drm] Skip scheduling IBs!
Jan 23 22:04:36 tiana kernel: [ 3083.223544] [drm] Skip scheduling IBs!
Jan 23 22:04:36 tiana kernel: [ 3083.223546] [drm] Skip scheduling IBs!
Jan 23 22:04:36 tiana kernel: [ 3083.223549] [drm] Skip scheduling IBs!
Jan 23 22:04:36 tiana kernel: [ 3083.223550] [drm] Skip scheduling IBs!
Jan 23 22:04:36 tiana kernel: [ 3083.223552] [drm] Skip scheduling IBs!
Jan 23 22:04:36 tiana kernel: [ 3083.223553] [drm] Skip scheduling IBs!
Jan 23 22:04:36 tiana kernel: [ 3083.223555] [drm] Skip scheduling IBs!
Jan 23 22:04:36 tiana kernel: [ 3083.223556] [drm] Skip scheduling IBs!
Jan 23 22:04:36 tiana kernel: [ 3083.223558] [drm] Skip scheduling IBs!
Jan 23 22:04:36 tiana kernel: [ 3083.223559] [drm] Skip scheduling IBs!
Jan 23 22:04:36 tiana kernel: [ 3083.223561] [drm] Skip scheduling IBs!
Jan 23 22:04:36 tiana kernel: [ 3083.223562] [drm] Skip scheduling IBs!
Jan 23 22:04:36 tiana kernel: [ 3083.223564] [drm] Skip scheduling IBs!
Jan 23 22:04:36 tiana kernel: [ 3083.223566] [drm] Skip scheduling IBs!
Jan 23 22:04:36 tiana kernel: [ 3083.223568] [drm] Skip scheduling IBs!
Jan 23 22:04:36 tiana kernel: [ 3083.223570] [drm] Skip scheduling IBs!
Jan 23 22:04:36 tiana kernel: [ 3083.223571] [drm] Skip scheduling IBs!
Jan 23 22:04:36 tiana kernel: [ 3083.223573] [drm] Skip scheduling IBs!
Jan 23 22:04:36 tiana kernel: [ 3083.223575] [drm] Skip scheduling IBs!
Jan 23 22:04:36 tiana kernel: [ 3083.223576] [drm] Skip scheduling IBs!
Jan 23 22:04:36 tiana kernel: [ 3083.223578] [drm] Skip scheduling IBs!
Jan 23 22:04:36 tiana kernel: [ 3083.223581] [drm] Skip scheduling IBs!
Jan 23 22:04:36 tiana kernel: [ 3083.223582] [drm] Skip scheduling IBs!
Jan 23 22:04:36 tiana kernel: [ 3083.223584] [drm] Skip scheduling IBs!
Jan 23 22:04:36 tiana kernel: [ 3083.223586] [drm] Skip scheduling IBs!
Jan 23 22:04:36 tiana kernel: [ 3083.223587] [drm] Skip scheduling IBs!
Jan 23 22:04:36 tiana kernel: [ 3083.223589] [drm] Skip scheduling IBs!
Jan 23 22:04:36 tiana kernel: [ 3083.223590] [drm] Skip scheduling IBs!
Jan 23 22:04:36 tiana kernel: [ 3083.223592] [drm] Skip scheduling IBs!
Jan 23 22:04:36 tiana kernel: [ 3083.223594] [drm] Skip scheduling IBs!
Jan 23 22:04:36 tiana kernel: [ 3083.223604] [drm] Skip scheduling IBs!
Jan 23 22:04:36 tiana kernel: [ 3083.223606] [drm] Skip scheduling IBs!
Jan 23 22:04:36 tiana kernel: [ 3083.223607] [drm] Skip scheduling IBs!
Jan 23 22:04:36 tiana kernel: [ 3083.223609] [drm] Skip scheduling IBs!
Jan 23 22:04:36 tiana kernel: [ 3083.223611] [drm] Skip scheduling IBs!
Jan 23 22:04:36 tiana kernel: [ 3083.223613] [drm] Skip scheduling IBs!
Jan 23 22:04:36 tiana kernel: [ 3083.223614] [drm] Skip scheduling IBs!
Jan 23 22:04:36 tiana kernel: [ 3083.223616] [drm] Skip scheduling IBs!
Jan 23 22:04:36 tiana kernel: [ 3083.223618] [drm] Skip scheduling IBs!
Jan 23 22:04:36 tiana kernel: [ 3083.223619] [drm] Skip scheduling IBs!
Jan 23 22:04:36 tiana kernel: [ 3083.223621] [drm] Skip scheduling IBs!
Jan 23 22:04:36 tiana kernel: [ 3083.223622] [drm] Skip scheduling IBs!
Jan 23 22:04:36 tiana kernel: [ 3083.223624] [drm] Skip scheduling IBs!
Jan 23 22:04:36 tiana kernel: [ 3083.223626] [drm] Skip scheduling IBs!
Jan 23 22:04:36 tiana kernel: [ 3083.223627] [drm] Skip scheduling IBs!
Jan 23 22:04:36 tiana kernel: [ 3083.223629] [drm] Skip scheduling IBs!
Jan 23 22:04:36 tiana kernel: [ 3083.223631] [drm] Skip scheduling IBs!
Jan 23 22:04:36 tiana kernel: [ 3083.223633] [drm] Skip scheduling IBs!
Jan 23 22:04:36 tiana kernel: [ 3083.223635] [drm] Skip scheduling IBs!
Jan 23 22:04:36 tiana kernel: [ 3083.223636] [drm] Skip scheduling IBs!
Jan 23 22:04:36 tiana kernel: [ 3083.223638] [drm] Skip scheduling IBs!
Jan 23 22:04:36 tiana kernel: [ 3083.223639] [drm] Skip scheduling IBs!
Jan 23 22:04:36 tiana kernel: [ 3083.223641] [drm] Skip scheduling IBs!
Jan 23 22:04:36 tiana kernel: [ 3083.223642] [drm] Skip scheduling IBs!
Jan 23 22:04:36 tiana kernel: [ 3083.223644] [drm] Skip scheduling IBs!
Jan 23 22:04:36 tiana kernel: [ 3083.223646] [drm] Skip scheduling IBs!
Jan 23 22:04:36 tiana kernel: [ 3083.223647] [drm] Skip scheduling IBs!
Jan 23 22:04:36 tiana kernel: [ 3083.223649] [drm] Skip scheduling IBs!
Jan 23 22:04:36 tiana kernel: [ 3083.223650] [drm] Skip scheduling IBs!
Jan 23 22:04:36 tiana kernel: [ 3083.223652] [drm] Skip scheduling IBs!
Jan 23 22:04:36 tiana kernel: [ 3083.223653] [drm] Skip scheduling IBs!
Jan 23 22:04:36 tiana kernel: [ 3083.223655] [drm] Skip scheduling IBs!
Jan 23 22:04:36 tiana kernel: [ 3083.223656] [drm] Skip scheduling IBs!
Jan 23 22:04:36 tiana kernel: [ 3083.223658] [drm] Skip scheduling IBs!
Jan 23 22:04:36 tiana kernel: [ 3083.223659] [drm] Skip scheduling IBs!
Jan 23 22:04:36 tiana kernel: [ 3083.223661] [drm] Skip scheduling IBs!
Jan 23 22:04:36 tiana kernel: [ 3083.223662] [drm] Skip scheduling IBs!
Jan 23 22:04:36 tiana kernel: [ 3083.223664] [drm] Skip scheduling IBs!
Jan 23 22:04:36 tiana kernel: [ 3083.223666] [drm] Skip scheduling IBs!
Jan 23 22:04:36 tiana kernel: [ 3083.223667] [drm] Skip scheduling IBs!
Jan 23 22:04:36 tiana kernel: [ 3083.223669] [drm] Skip scheduling IBs!
Jan 23 22:04:36 tiana kernel: [ 3083.223671] [drm] Skip scheduling IBs!
Jan 23 22:04:36 tiana kernel: [ 3083.223672] [drm] Skip scheduling IBs!
Jan 23 22:04:36 tiana kernel: [ 3083.223674] [drm] Skip scheduling IBs!
Jan 23 22:04:36 tiana kernel: [ 3083.223676] [drm] Skip scheduling IBs!
Jan 23 22:04:36 tiana kernel: [ 3083.223678] [drm] Skip scheduling IBs!
Jan 23 22:04:36 tiana kernel: [ 3083.223679] [drm] Skip scheduling IBs!
Jan 23 22:04:36 tiana kernel: [ 3083.223681] [drm] Skip scheduling IBs!
Jan 23 22:04:36 tiana kernel: [ 3083.223683] [drm] Skip scheduling IBs!
Jan 23 22:04:36 tiana kernel: [ 3083.223684] [drm] Skip scheduling IBs!
Jan 23 22:04:36 tiana kernel: [ 3083.223686] [drm] Skip scheduling IBs!
Jan 23 22:04:36 tiana kernel: [ 3083.223688] [drm] Skip scheduling IBs!
Jan 23 22:04:36 tiana kernel: [ 3083.223690] [drm] Skip scheduling IBs!
Jan 23 22:04:36 tiana kernel: [ 3083.223691] [drm] Skip scheduling IBs!
Jan 23 22:04:36 tiana kernel: [ 3083.223693] [drm] Skip scheduling IBs!
Jan 23 22:04:36 tiana kernel: [ 3083.223695] [drm] Skip scheduling IBs!
Jan 23 22:04:36 tiana kernel: [ 3083.223697] [drm] Skip scheduling IBs!
Jan 23 22:04:36 tiana kernel: [ 3083.223698] [drm] Skip scheduling IBs!
Jan 23 22:04:36 tiana kernel: [ 3083.223700] [drm] Skip scheduling IBs!
Jan 23 22:04:36 tiana kernel: [ 3083.223702] [drm] Skip scheduling IBs!
Jan 23 22:04:36 tiana kernel: [ 3083.223703] [drm] Skip scheduling IBs!
Jan 23 22:04:36 tiana kernel: [ 3083.223705] [drm] Skip scheduling IBs!
Jan 23 22:04:36 tiana kernel: [ 3083.223706] [drm] Skip scheduling IBs!
Jan 23 22:04:36 tiana kernel: [ 3083.223708] [drm] Skip scheduling IBs!
Jan 23 22:04:36 tiana kernel: [ 3083.223709] [drm] Skip scheduling IBs!
Jan 23 22:04:36 tiana kernel: [ 3083.223711] [drm] Skip scheduling IBs!
Jan 23 22:04:36 tiana kernel: [ 3083.223712] [drm] Skip scheduling IBs!
Jan 23 22:04:36 tiana kernel: [ 3083.223714] [drm] Skip scheduling IBs!
Jan 23 22:04:36 tiana kernel: [ 3083.223716] [drm] Skip scheduling IBs!
Jan 23 22:04:36 tiana kernel: [ 3083.223717] [drm] Skip scheduling IBs!
Jan 23 22:04:36 tiana kernel: [ 3083.223720] [drm] Skip scheduling IBs!
Jan 23 22:04:36 tiana kernel: [ 3083.223722] [drm] Skip scheduling IBs!
Jan 23 22:04:36 tiana kernel: [ 3083.223724] [drm] Skip scheduling IBs!
Jan 23 22:04:36 tiana kernel: [ 3083.223726] [drm] Skip scheduling IBs!
Jan 23 22:04:36 tiana kernel: [ 3083.223727] [drm] Skip scheduling IBs!
Jan 23 22:04:36 tiana kernel: [ 3083.223729] [drm] Skip scheduling IBs!
Jan 23 22:04:36 tiana kernel: [ 3083.223730] [drm] Skip scheduling IBs!
Jan 23 22:04:36 tiana kernel: [ 3083.223732] [drm] Skip scheduling IBs!
Jan 23 22:04:36 tiana kernel: [ 3083.223734] [drm] Skip scheduling IBs!
Jan 23 22:04:36 tiana kernel: [ 3083.223736] [drm] Skip scheduling IBs!
Jan 23 22:04:36 tiana kernel: [ 3083.223738] [drm] Skip scheduling IBs!
Jan 23 22:04:36 tiana kernel: [ 3083.223739] [drm] Skip scheduling IBs!
Jan 23 22:04:36 tiana kernel: [ 3083.223741] [drm] Skip scheduling IBs!
Jan 23 22:04:36 tiana kernel: [ 3083.223742] [drm] Skip scheduling IBs!
Jan 23 22:04:36 tiana kernel: [ 3083.223744] [drm] Skip scheduling IBs!
Jan 23 22:04:36 tiana kernel: [ 3083.223745] [drm] Skip scheduling IBs!
Jan 23 22:04:36 tiana kernel: [ 3083.223747] [drm] Skip scheduling IBs!
Jan 23 22:04:36 tiana kernel: [ 3083.223748] [drm] Skip scheduling IBs!
Jan 23 22:04:36 tiana kernel: [ 3083.223750] [drm] Skip scheduling IBs!
Jan 23 22:04:36 tiana kernel: [ 3083.223752] [drm] Skip scheduling IBs!
Jan 23 22:04:36 tiana kernel: [ 3083.223753] [drm] Skip scheduling IBs!
Jan 23 22:04:36 tiana kernel: [ 3083.223755] [drm] Skip scheduling IBs!
Jan 23 22:04:36 tiana kernel: [ 3083.223756] [drm] Skip scheduling IBs!
Jan 23 22:04:36 tiana kernel: [ 3083.223758] [drm] Skip scheduling IBs!
Jan 23 22:04:36 tiana kernel: [ 3083.223760] [drm] Skip scheduling IBs!
Jan 23 22:04:36 tiana kernel: [ 3083.223761] [drm] Skip scheduling IBs!
Jan 23 22:04:36 tiana kernel: [ 3083.223763] [drm] Skip scheduling IBs!
Jan 23 22:04:36 tiana kernel: [ 3083.223764] [drm] Skip scheduling IBs!
Jan 23 22:04:36 tiana kernel: [ 3083.223766] [drm] Skip scheduling IBs!
Jan 23 22:04:36 tiana kernel: [ 3083.223767] [drm] Skip scheduling IBs!
Jan 23 22:04:36 tiana kernel: [ 3083.223768] [drm] Skip scheduling IBs!
Jan 23 22:04:36 tiana kernel: [ 3083.223770] [drm] Skip scheduling IBs!
Jan 23 22:04:36 tiana kernel: [ 3083.223772] [drm] Skip scheduling IBs!
Jan 23 22:04:36 tiana kernel: [ 3083.223773] [drm] Skip scheduling IBs!
Jan 23 22:04:36 tiana kernel: [ 3083.223775] [drm] Skip scheduling IBs!
Jan 23 22:04:36 tiana kernel: [ 3083.223776] [drm] Skip scheduling IBs!
Jan 23 22:04:36 tiana kernel: [ 3083.223778] [drm] Skip scheduling IBs!
Jan 23 22:04:36 tiana kernel: [ 3083.223779] [drm] Skip scheduling IBs!
Jan 23 22:04:36 tiana kernel: [ 3083.223781] [drm] Skip scheduling IBs!
Jan 23 22:04:36 tiana kernel: [ 3083.223783] [drm] Skip scheduling IBs!
Jan 23 22:04:36 tiana kernel: [ 3083.223784] [drm] Skip scheduling IBs!
Jan 23 22:04:36 tiana kernel: [ 3083.223786] [drm] Skip scheduling IBs!
Jan 23 22:04:36 tiana kernel: [ 3083.223787] [drm] Skip scheduling IBs!
Jan 23 22:07:39 tiana kernel: [    0.000000] Linux version 5.10.0-11-amd64 (debian-kernel@lists.debian.org) (gcc-10 (Debian 10.2.1-6) 10.2.1 20210110, GNU ld (GNU Binutils for Debian) 2.35.2) #1 SMP Debian 5.10.92-1 (2022-01-18)
```

</details>


### 2

<details><summary>kern.log</summary>

```
Jan 24 00:41:36 tiana kernel: [ 6264.803554] [drm:amdgpu_dm_atomic_commit_tail [amdgpu]] *ERROR* Waiting for fences timed out!
Jan 24 00:41:36 tiana kernel: [ 6269.923517] [drm:amdgpu_job_timedout [amdgpu]] *ERROR* ring page0 timeout, signaled seq=47312, emitted seq=47325
Jan 24 00:41:36 tiana kernel: [ 6269.923635] [drm:amdgpu_dm_atomic_commit_tail [amdgpu]] *ERROR* Waiting for fences timed out!
Jan 24 00:41:36 tiana kernel: [ 6269.923686] [drm:amdgpu_job_timedout [amdgpu]] *ERROR* Process information: process  pid 0 thread  pid 0
Jan 24 00:41:36 tiana kernel: [ 6269.923689] amdgpu 0000:2b:00.0: amdgpu: GPU reset begin!
Jan 24 00:41:45 tiana kernel: [ 6275.043656] [drm:amdgpu_dm_atomic_commit_tail [amdgpu]] *ERROR* Waiting for fences timed out!
Jan 24 00:41:45 tiana kernel: [ 6278.927587] qcm fence wait loop timeout expired
Jan 24 00:41:45 tiana kernel: [ 6278.927590] The cp might be in an unrecoverable state due to an unsuccessful queues preemption
Jan 24 00:41:45 tiana kernel: [ 6278.927591] amdgpu: Failed to evict process queues
Jan 24 00:41:45 tiana kernel: [ 6278.927592] amdgpu: Failed to suspend process 0x800d
Jan 24 00:41:46 tiana kernel: [ 6279.167598] [drm] psp command (0x2) failed and response status is (0x117)
Jan 24 00:41:46 tiana kernel: [ 6279.167600] [drm] free PSP TMR buffer
Jan 24 00:41:46 tiana kernel: [ 6279.200515] amdgpu 0000:2b:00.0: amdgpu: BACO reset
Jan 24 00:41:46 tiana kernel: [ 6279.749691] amdgpu 0000:2b:00.0: amdgpu: GPU reset succeeded, trying to resume
Jan 24 00:41:46 tiana kernel: [ 6279.749865] [drm] PCIE GART of 512M enabled (table at 0x000000F400900000).
Jan 24 00:41:46 tiana kernel: [ 6279.749886] [drm] VRAM is lost due to GPU reset!
Jan 24 00:41:46 tiana kernel: [ 6279.750163] [drm] PSP is resuming...
Jan 24 00:41:46 tiana kernel: [ 6279.937218] [drm] reserve 0x400000 from 0xf7fec00000 for PSP TMR
Jan 24 00:41:47 tiana kernel: [ 6280.117413] [drm] kiq ring mec 2 pipe 1 q 0
Jan 24 00:41:47 tiana kernel: [ 6280.163735] [drm:amdgpu_dm_atomic_commit_tail [amdgpu]] *ERROR* Waiting for fences timed out!
Jan 24 00:41:47 tiana kernel: [ 6280.229888] [drm] UVD and UVD ENC initialized successfully.
Jan 24 00:41:47 tiana kernel: [ 6280.329541] [drm] VCE initialized successfully.
Jan 24 00:41:47 tiana kernel: [ 6280.329560] amdgpu 0000:2b:00.0: amdgpu: ring gfx uses VM inv eng 0 on hub 0
Jan 24 00:41:47 tiana kernel: [ 6280.329561] amdgpu 0000:2b:00.0: amdgpu: ring comp_1.0.0 uses VM inv eng 1 on hub 0
Jan 24 00:41:47 tiana kernel: [ 6280.329562] amdgpu 0000:2b:00.0: amdgpu: ring comp_1.1.0 uses VM inv eng 4 on hub 0
Jan 24 00:41:47 tiana kernel: [ 6280.329563] amdgpu 0000:2b:00.0: amdgpu: ring comp_1.2.0 uses VM inv eng 5 on hub 0
Jan 24 00:41:47 tiana kernel: [ 6280.329563] amdgpu 0000:2b:00.0: amdgpu: ring comp_1.3.0 uses VM inv eng 6 on hub 0
Jan 24 00:41:47 tiana kernel: [ 6280.329564] amdgpu 0000:2b:00.0: amdgpu: ring comp_1.0.1 uses VM inv eng 7 on hub 0
Jan 24 00:41:47 tiana kernel: [ 6280.329565] amdgpu 0000:2b:00.0: amdgpu: ring comp_1.1.1 uses VM inv eng 8 on hub 0
Jan 24 00:41:47 tiana kernel: [ 6280.329565] amdgpu 0000:2b:00.0: amdgpu: ring comp_1.2.1 uses VM inv eng 9 on hub 0
Jan 24 00:41:47 tiana kernel: [ 6280.329566] amdgpu 0000:2b:00.0: amdgpu: ring comp_1.3.1 uses VM inv eng 10 on hub 0
Jan 24 00:41:47 tiana kernel: [ 6280.329567] amdgpu 0000:2b:00.0: amdgpu: ring kiq_2.1.0 uses VM inv eng 11 on hub 0
Jan 24 00:41:47 tiana kernel: [ 6280.329567] amdgpu 0000:2b:00.0: amdgpu: ring sdma0 uses VM inv eng 0 on hub 1
Jan 24 00:41:47 tiana kernel: [ 6280.329568] amdgpu 0000:2b:00.0: amdgpu: ring page0 uses VM inv eng 1 on hub 1
Jan 24 00:41:47 tiana kernel: [ 6280.329569] amdgpu 0000:2b:00.0: amdgpu: ring sdma1 uses VM inv eng 4 on hub 1
Jan 24 00:41:47 tiana kernel: [ 6280.329569] amdgpu 0000:2b:00.0: amdgpu: ring page1 uses VM inv eng 5 on hub 1
Jan 24 00:41:47 tiana kernel: [ 6280.329570] amdgpu 0000:2b:00.0: amdgpu: ring uvd_0 uses VM inv eng 6 on hub 1
Jan 24 00:41:47 tiana kernel: [ 6280.329571] amdgpu 0000:2b:00.0: amdgpu: ring uvd_enc_0.0 uses VM inv eng 7 on hub 1
Jan 24 00:41:47 tiana kernel: [ 6280.329571] amdgpu 0000:2b:00.0: amdgpu: ring uvd_enc_0.1 uses VM inv eng 8 on hub 1
Jan 24 00:41:47 tiana kernel: [ 6280.329572] amdgpu 0000:2b:00.0: amdgpu: ring vce0 uses VM inv eng 9 on hub 1
Jan 24 00:41:47 tiana kernel: [ 6280.329572] amdgpu 0000:2b:00.0: amdgpu: ring vce1 uses VM inv eng 10 on hub 1
Jan 24 00:41:47 tiana kernel: [ 6280.329573] amdgpu 0000:2b:00.0: amdgpu: ring vce2 uses VM inv eng 11 on hub 1
Jan 24 00:41:47 tiana kernel: [ 6280.331419] amdgpu 0000:2b:00.0: amdgpu: recover vram bo from shadow start
Jan 24 00:41:47 tiana kernel: [ 6280.332599] amdgpu 0000:2b:00.0: amdgpu: recover vram bo from shadow done
Jan 24 00:41:47 tiana kernel: [ 6280.332607] [drm] Skip scheduling IBs!
Jan 24 00:41:47 tiana kernel: [ 6280.332607] [drm] Skip scheduling IBs!
Jan 24 00:41:47 tiana kernel: [ 6280.332608] [drm] Skip scheduling IBs!
Jan 24 00:41:47 tiana kernel: [ 6280.332608] [drm] Skip scheduling IBs!
Jan 24 00:41:47 tiana kernel: [ 6280.332609] [drm] Skip scheduling IBs!
Jan 24 00:41:47 tiana kernel: [ 6280.332610] [drm] Skip scheduling IBs!
Jan 24 00:41:47 tiana kernel: [ 6280.332610] [drm] Skip scheduling IBs!
Jan 24 00:41:47 tiana kernel: [ 6280.332611] [drm] Skip scheduling IBs!
Jan 24 00:41:47 tiana kernel: [ 6280.332611] [drm] Skip scheduling IBs!
Jan 24 00:41:47 tiana kernel: [ 6280.332612] [drm] Skip scheduling IBs!
Jan 24 00:41:47 tiana kernel: [ 6280.332612] [drm] Skip scheduling IBs!
Jan 24 00:41:47 tiana kernel: [ 6280.332613] [drm] Skip scheduling IBs!
Jan 24 00:41:47 tiana kernel: [ 6280.332614] [drm] Skip scheduling IBs!
Jan 24 00:41:47 tiana kernel: [ 6280.332621] amdgpu 0000:2b:00.0: amdgpu: GPU reset(1) succeeded!
Jan 24 00:41:47 tiana kernel: [ 6280.332624] [drm] Skip scheduling IBs!
Jan 24 00:41:47 tiana kernel: [ 6280.332630] [drm] Skip scheduling IBs!
Jan 24 00:41:47 tiana kernel: [ 6280.332634] [drm] Skip scheduling IBs!
Jan 24 00:41:47 tiana kernel: [ 6280.332650] [drm] Skip scheduling IBs!
Jan 24 00:54:22 tiana kernel: [    0.000000] Linux version 5.10.0-11-amd64 (debian-kernel@lists.debian.org) (gcc-10 (Debian 10.2.1-6) 10.2.1 20210110, GNU ld (GNU Binutils for Debian) 2.35.2) #1 SMP Debian 5.10.92-1 (2022-01-18)
```

</details>

## soft crashes

### 1
tensorflow ended training session, terminal reported "Aborted". System still responsive.

<details><summary>kern.log</summary>

```
Jan 23 22:42:37 tiana kernel: [ 1750.417261] amdgpu 0000:2b:00.0: amdgpu: [mmhub0] retry page fault (src_id:0 ring:0 vmid:8 pasid:32776, for process python pid 39924 thread python pid 39924)
Jan 23 22:42:37 tiana kernel: [ 1750.417270] amdgpu 0000:2b:00.0: amdgpu:   in page starting at address 0x00005fc427468000 from client 18
Jan 23 22:42:37 tiana kernel: [ 1750.417272] amdgpu 0000:2b:00.0: amdgpu: VM_L2_PROTECTION_FAULT_STATUS:0x00840051
Jan 23 22:42:37 tiana kernel: [ 1750.417274] amdgpu 0000:2b:00.0: amdgpu:        Faulty UTCL2 client ID: MP0 (0x0)
Jan 23 22:42:37 tiana kernel: [ 1750.417275] amdgpu 0000:2b:00.0: amdgpu:        MORE_FAULTS: 0x1
Jan 23 22:42:37 tiana kernel: [ 1750.417276] amdgpu 0000:2b:00.0: amdgpu:        WALKER_ERROR: 0x0
Jan 23 22:42:37 tiana kernel: [ 1750.417277] amdgpu 0000:2b:00.0: amdgpu:        PERMISSION_FAULTS: 0x5
Jan 23 22:42:37 tiana kernel: [ 1750.417279] amdgpu 0000:2b:00.0: amdgpu:        MAPPING_ERROR: 0x0
Jan 23 22:42:37 tiana kernel: [ 1750.417280] amdgpu 0000:2b:00.0: amdgpu:        RW: 0x1
Jan 23 22:42:37 tiana kernel: [ 1750.417288] amdgpu 0000:2b:00.0: amdgpu: [mmhub0] retry page fault (src_id:0 ring:0 vmid:8 pasid:32776, for process python pid 39924 thread python pid 39924)
Jan 23 22:42:37 tiana kernel: [ 1750.417289] amdgpu 0000:2b:00.0: amdgpu:   in page starting at address 0x00005fc427469000 from client 18
Jan 23 22:42:37 tiana kernel: [ 1750.417290] amdgpu 0000:2b:00.0: amdgpu: VM_L2_PROTECTION_FAULT_STATUS:0x00000000
Jan 23 22:42:37 tiana kernel: [ 1750.417291] amdgpu 0000:2b:00.0: amdgpu:        Faulty UTCL2 client ID: MP0 (0x0)
Jan 23 22:42:37 tiana kernel: [ 1750.417292] amdgpu 0000:2b:00.0: amdgpu:        MORE_FAULTS: 0x0
Jan 23 22:42:37 tiana kernel: [ 1750.417293] amdgpu 0000:2b:00.0: amdgpu:        WALKER_ERROR: 0x0
Jan 23 22:42:37 tiana kernel: [ 1750.417294] amdgpu 0000:2b:00.0: amdgpu:        PERMISSION_FAULTS: 0x0
Jan 23 22:42:37 tiana kernel: [ 1750.417295] amdgpu 0000:2b:00.0: amdgpu:        MAPPING_ERROR: 0x0
Jan 23 22:42:37 tiana kernel: [ 1750.417296] amdgpu 0000:2b:00.0: amdgpu:        RW: 0x0
Jan 23 22:42:37 tiana kernel: [ 1750.417303] amdgpu 0000:2b:00.0: amdgpu: [mmhub0] retry page fault (src_id:0 ring:0 vmid:8 pasid:32776, for process python pid 39924 thread python pid 39924)
Jan 23 22:42:37 tiana kernel: [ 1750.417304] amdgpu 0000:2b:00.0: amdgpu:   in page starting at address 0x00005fc42746a000 from client 18
Jan 23 22:42:37 tiana kernel: [ 1750.417304] amdgpu 0000:2b:00.0: amdgpu: VM_L2_PROTECTION_FAULT_STATUS:0x00000000
Jan 23 22:42:37 tiana kernel: [ 1750.417305] amdgpu 0000:2b:00.0: amdgpu:        Faulty UTCL2 client ID: MP0 (0x0)
Jan 23 22:42:37 tiana kernel: [ 1750.417306] amdgpu 0000:2b:00.0: amdgpu:        MORE_FAULTS: 0x0
Jan 23 22:42:37 tiana kernel: [ 1750.417307] amdgpu 0000:2b:00.0: amdgpu:        WALKER_ERROR: 0x0
Jan 23 22:42:37 tiana kernel: [ 1750.417308] amd
kern.loggpu 0000:2b:00.0: amdgpu:   in page starting at address 0x00005fc42746b000 from client 18
Jan 23 22:42:37 tiana kernel: [ 1750.417318] amdgpu 0000:2b:00.0: amdgpu: VM_L2_PROTECTION_FAULT_STATUS:0x00000000
Jan 23 22:42:37 tiana kernel: [ 1750.417319] amdgpu 0000:2b:00.0: amdgpu:        Faulty UTCL2 client ID: MP0 (0x0)
Jan 23 22:42:37 tiana kernel: [ 1750.417319] amdgpu 0000:2b:00.0: amdgpu:        MORE_FAULTS: 0x0
Jan 23 22:42:37 tiana kernel: [ 1750.417320] amdgpu 0000:2b:00.0: amdgpu:        WALKER_ERROR: 0x0
Jan 23 22:42:37 tiana kernel: [ 1750.417321] amdgpu 0000:2b:00.0: amdgpu:        PERMISSION_FAULTS: 0x0
Jan 23 22:42:37 tiana kernel: [ 1750.417321] amdgpu 0000:2b:00.0: amdgpu:        MAPPING_ERROR: 0x0
Jan 23 22:42:37 tiana kernel: [ 1750.417322] amdgpu 0000:2b:00.0: amdgpu:        RW: 0x0
Jan 23 22:42:37 tiana kernel: [ 1750.417329] amdgpu 0000:2b:00.0: amdgpu: [mmhub0] retry page fault (src_id:0 ring:0 vmid:8 pasid:32776, for process python pid 39924 thread python pid 39924)
Jan 23 22:42:37 tiana kernel: [ 1750.417330] amdgpu 0000:2b:00.0: amdgpu:   in page starting at address 0x00005fc42746c000 from client 18
Jan 23 22:42:37 tiana kernel: [ 1750.417331] amdgpu 0000:2b:00.0: amdgpu: VM_L2_PROTECTION_FAULT_STATUS:0x00000000
Jan 23 22:42:37 tiana kernel: [ 1750.417331] amdgpu 0000:2b:00.0: amdgpu:        Faulty UTCL2 client ID: MP0 (0x0)
Jan 23 22:42:37 tiana kernel: [ 1750.417332] amdgpu 0000:2b:00.0: amdgpu:        MORE_FAULTS: 0x0
Jan 23 22:42:37 tiana kernel: [ 1750.417333] amdgpu 0000:2b:00.0: amdgpu:        WALKER_ERROR: 0x0
Jan 23 22:42:37 tiana kernel: [ 1750.417334] amdgpu 0000:2b:00.0: amdgpu:        PERMISSION_FAULTS: 0x0
Jan 23 22:42:37 tiana kernel: [ 1750.417334] amdgpu 0000:2b:00.0: amdgpu:        MAPPING_ERROR: 0x0
Jan 23 22:42:37 tiana kernel: [ 1750.417335] amdgpu 0000:2b:00.0: amdgpu:        RW: 0x0
Jan 23 22:42:37 tiana kernel: [ 1750.417341] amdgpu 0000:2b:00.0: amdgpu: [mmhub0] retry page fault (src_id:0 ring:0 vmid:8 pasid:32776, for process python pid 39924 thread python pid 39924)
Jan 23 22:42:37 tiana kernel: [ 1750.417342] amdgpu 0000:2b:00.0: amdgpu:   in page starting at address 0x00005fc42746d000 from client 18
Jan 23 22:42:37 tiana kernel: [ 1750.417343] amdgpu 0000:2b:00.0: amdgpu: VM_L2_PROTECTION_FAULT_STATUS:0x00000000
Jan 23 22:42:37 tiana kernel: [ 1750.417344] amdgpu 0000:2b:00.0: amdgpu:        Faulty UTCL2 client ID: MP0 (0x0)
Jan 23 22:42:37 tiana kernel: [ 1750.417344] amdgpu 0000:2b:00.0: amdgpu:        MORE_FAULTS: 0x0
Jan 23 22:42:37 tiana kernel: [ 1750.417345] amdgpu 0000:2b:00.0: amdgpu:        WALKER_ERROR: 0x0
Jan 23 22:42:37 tiana kernel: [ 1750.417346] amdgpu 0000:2b:00.0: amdgpu:        PERMISSION_FAULTS: 0x0
Jan 23 22:42:37 tiana kernel: [ 1750.417347] amdgpu 0000:2b:00.0: amdgpu:        MAPPING_ERROR: 0x0
Jan 23 22:42:37 tiana kernel: [ 1750.417347] amdgpu 0000:2b:00.0: amdgpu:        RW: 0x0
Jan 23 22:42:37 tiana kernel: [ 1750.417354] amd
kern.loggpu 0000:2b:00.0: amdgpu:   in page starting at address 0x00005fc42746e000 from client 18
Jan 23 22:42:37 tiana kernel: [ 1750.417355] amdgpu 0000:2b:00.0: amdgpu: VM_L2_PROTECTION_FAULT_STATUS:0x00000000
Jan 23 22:42:37 tiana kernel: [ 1750.417356] amdgpu 0000:2b:00.0: amdgpu:        Faulty UTCL2 client ID: MP0 (0x0)
Jan 23 22:42:37 tiana kernel: [ 1750.417357] amdgpu 0000:2b:00.0: amdgpu:        MORE_FAULTS: 0x0
Jan 23 22:42:37 tiana kernel: [ 1750.417358] amdgpu 0000:2b:00.0: amdgpu:        WALKER_ERROR: 0x0
Jan 23 22:42:37 tiana kernel: [ 1750.417358] amdgpu 0000:2b:00.0: amdgpu:        PERMISSION_FAULTS: 0x0
Jan 23 22:42:37 tiana kernel: [ 1750.417359] amdgpu 0000:2b:00.0: amdgpu:        MAPPING_ERROR: 0x0
Jan 23 22:42:37 tiana kernel: [ 1750.417360] amdgpu 0000:2b:00.0: amdgpu:        RW: 0x0
```

</details>

### 2

terminal response
```
...
Epoch 36/200
42/42 [==============================] - 11s 258ms/step - loss: 0.0020 - accuracy: 1.0000 - val_loss: 0.5028 - val_accuracy: 0.8803
Epoch 37/200
 4/42 [=>............................] - ETA: 14s - loss: 0.0016 - accuracy: 1.0000Memory access fault by GPU node-1 (Agent handle: 0x4ef7c60) on address 0x3e6ca840e000. Reason: Page not present or supervisor privilege.
Aborted
```

<details><summary>kern.log</summary>

```
Jan 23 23:07:32 tiana kernel: [  625.063869] gmc_v9_0_process_interrupt: 3 callbacks suppressed
Jan 23 23:07:32 tiana kernel: [  625.063875] amdgpu 0000:2b:00.0: amdgpu: [mmhub0] retry page fault (src_id:0 ring:0 vmid:8 pasid:32777, for process python pid 4381 thread python pid 4381)
Jan 23 23:07:32 tiana kernel: [  625.063881] amdgpu 0000:2b:00.0: amdgpu:   in page starting at address 0x00003e6ca840e000 from client 18
Jan 23 23:07:32 tiana kernel: [  625.063893] amdgpu 0000:2b:00.0: amdgpu: VM_L2_PROTECTION_FAULT_STATUS:0x00800031
Jan 23 23:07:32 tiana kernel: [  625.063896] amdgpu 0000:2b:00.0: amdgpu:        Faulty UTCL2 client ID: MP0 (0x0)
Jan 23 23:07:32 tiana kernel: [  625.063898] amdgpu 0000:2b:00.0: amdgpu:        MORE_FAULTS: 0x1
Jan 23 23:07:32 tiana kernel: [  625.063899] amdgpu 0000:2b:00.0: amdgpu:        WALKER_ERROR: 0x0
Jan 23 23:07:32 tiana kernel: [  625.063901] amdgpu 0000:2b:00.0: amdgpu:        PERMISSION_FAULTS: 0x3
Jan 23 23:07:32 tiana kernel: [  625.063907] amdgpu 0000:2b:00.0: amdgpu:        MAPPING_ERROR: 0x0
Jan 23 23:07:32 tiana kernel: [  625.063908] amdgpu 0000:2b:00.0: amdgpu:        RW: 0x0
Jan 23 23:07:32 tiana kernel: [  625.063940] amdgpu 0000:2b:00.0: amdgpu: [mmhub0] no-retry page fault (src_id:0 ring:157 vmid:8 pasid:32777, for process python pid 4381 thread python pid 4381)
Jan 23 23:07:32 tiana kernel: [  625.063942] amdgpu 0000:2b:00.0: amdgpu:   in page starting at address 0x00003e6ca840e000 from client 18
Jan 23 23:07:32 tiana kernel: [  625.063944] amdgpu 0000:2b:00.0: amdgpu: VM_L2_PROTECTION_FAULT_STATUS:0x00800031
Jan 23 23:07:32 tiana kernel: [  625.063946] amdgpu 0000:2b:00.0: amdgpu:        Faulty UTCL2 client ID: MP0 (0x0)
Jan 23 23:07:32 tiana kernel: [  625.063948] amdgpu 0000:2b:00.0: amdgpu:        MORE_FAULTS: 0x1
Jan 23 23:07:32 tiana kernel: [  625.063949] amdgpu 0000:2b:00.0: amdgpu:        WALKER_ERROR: 0x0
Jan 23 23:07:32 tiana kernel: [  625.063951] amdgpu 0000:2b:00.0: amdgpu:        PERMISSION_FAULTS: 0x3
Jan 23 23:07:32 tiana kernel: [  625.063953] amdgpu 0000:2b:00.0: amdgpu:        MAPPING_ERROR: 0x0
Jan 23 23:07:32 tiana kernel: [  625.063955] amdgpu 0000:2b:00.0: amdgpu:        RW: 0x0
```

</details>

<details>
  <summary>rocminfo</summary>

```
ROCk module is loaded
=====================    
HSA System Attributes    
=====================    
Runtime Version:         1.1
System Timestamp Freq.:  1000.000000MHz
Sig. Max Wait Duration:  18446744073709551615 (0xFFFFFFFFFFFFFFFF) (timestamp count)
Machine Model:           LARGE                              
System Endianness:       LITTLE                             

==========               
HSA Agents               
==========               
*******                  
Agent 1                  
*******                  
  Name:                    AMD Ryzen 7 3800X 8-Core Processor 
  Uuid:                    CPU-XX                             
  Marketing Name:          AMD Ryzen 7 3800X 8-Core Processor 
  Vendor Name:             CPU                                
  Feature:                 None specified                     
  Profile:                 FULL_PROFILE                       
  Float Round Mode:        NEAR                               
  Max Queue Number:        0(0x0)                             
  Queue Min Size:          0(0x0)                             
  Queue Max Size:          0(0x0)                             
  Queue Type:              MULTI                              
  Node:                    0                                  
  Device Type:             CPU                                
  Cache Info:              
    L1:                      32768(0x8000) KB                   
  Chip ID:                 0(0x0)                             
  Cacheline Size:          64(0x40)                           
  Max Clock Freq. (MHz):   3900                               
  BDFID:                   0                                  
  Internal Node ID:        0                                  
  Compute Unit:            16                                 
  SIMDs per CU:            0                                  
  Shader Engines:          0                                  
  Shader Arrs. per Eng.:   0                                  
  WatchPts on Addr. Ranges:1                                  
  Features:                None
  Pool Info:               
    Pool 1                   
      Segment:                 GLOBAL; FLAGS: FINE GRAINED        
      Size:                    32865812(0x1f57e14) KB             
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
    Pool 2                   
      Segment:                 GLOBAL; FLAGS: KERNARG, FINE GRAINED
      Size:                    32865812(0x1f57e14) KB             
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
    Pool 3                   
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED      
      Size:                    32865812(0x1f57e14) KB             
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       TRUE                               
  ISA Info:                
*******                  
Agent 2                  
*******                  
  Name:                    gfx900                             
  Uuid:                    GPU-0214fe94c6a64924               
  Marketing Name:          Radeon Vega Frontier Edition       
  Vendor Name:             AMD                                
  Feature:                 KERNEL_DISPATCH                    
  Profile:                 BASE_PROFILE                       
  Float Round Mode:        NEAR                               
  Max Queue Number:        128(0x80)                          
  Queue Min Size:          4096(0x1000)                       
  Queue Max Size:          131072(0x20000)                    
  Queue Type:              MULTI                              
  Node:                    1                                  
  Device Type:             GPU                                
  Cache Info:              
    L1:                      16(0x10) KB                        
  Chip ID:                 26723(0x6863)                      
  Cacheline Size:          64(0x40)                           
  Max Clock Freq. (MHz):   1600                               
  BDFID:                   11008                              
  Internal Node ID:        1                                  
  Compute Unit:            64                                 
  SIMDs per CU:            4                                  
  Shader Engines:          4                                  
  Shader Arrs. per Eng.:   1                                  
  WatchPts on Addr. Ranges:4                                  
  Features:                KERNEL_DISPATCH 
  Fast F16 Operation:      FALSE                              
  Wavefront Size:          64(0x40)                           
  Workgroup Max Size:      1024(0x400)                        
  Workgroup Max Size per Dimension:
    x                        1024(0x400)                        
    y                        1024(0x400)                        
    z                        1024(0x400)                        
  Max Waves Per CU:        40(0x28)                           
  Max Work-item Per CU:    2560(0xa00)                        
  Grid Max Size:           4294967295(0xffffffff)             
  Grid Max Size per Dimension:
    x                        4294967295(0xffffffff)             
    y                        4294967295(0xffffffff)             
    z                        4294967295(0xffffffff)             
  Max fbarriers/Workgrp:   32                                 
  Pool Info:               
    Pool 1                   
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED      
      Size:                    16760832(0xffc000) KB              
      Allocatable:             TRUE                               
      Alloc Granule:           4KB                                
      Alloc Alignment:         4KB                                
      Accessible by all:       FALSE                              
    Pool 2                   
      Segment:                 GROUP                              
      Size:                    64(0x40) KB                        
      Allocatable:             FALSE                              
      Alloc Granule:           0KB                                
      Alloc Alignment:         0KB                                
      Accessible by all:       FALSE                              
  ISA Info:                
    ISA 1                    
      Name:                    amdgcn-amd-amdhsa--gfx900:xnack-   
      Machine Models:          HSA_MACHINE_MODEL_LARGE            
      Profiles:                HSA_PROFILE_BASE                   
      Default Rounding Mode:   NEAR                               
      Default Rounding Mode:   NEAR                               
      Fast f16:                TRUE                               
      Workgroup Max Size:      1024(0x400)                        
      Workgroup Max Size per Dimension:
        x                        1024(0x400)                        
        y                        1024(0x400)                        
        z                        1024(0x400)                        
      Grid Max Size:           4294967295(0xffffffff)             
      Grid Max Size per Dimension:
        x                        4294967295(0xffffffff)             
        y                        4294967295(0xffffffff)             
        z                        4294967295(0xffffffff)             
      FBarrier Max Size:       32                                 
*** Done ***    
```

</details>


<details><summary>clinfo</summary>

```
Number of platforms                               1
  Platform Name                                   AMD Accelerated Parallel Processing
  Platform Vendor                                 Advanced Micro Devices, Inc.
  Platform Version                                OpenCL 2.2 AMD-APP (3361.0)
  Platform Profile                                FULL_PROFILE
  Platform Extensions                             cl_khr_icd cl_amd_event_callback 
  Platform Extensions function suffix             AMD
  Platform Host timer resolution                  1ns

  Platform Name                                   AMD Accelerated Parallel Processing
Number of devices                                 1
  Device Name                                     gfx900:xnack-
  Device Vendor                                   Advanced Micro Devices, Inc.
  Device Vendor ID                                0x1002
  Device Version                                  OpenCL 2.0 
  Driver Version                                  3361.0 (HSA1.1,LC)
  Device OpenCL C Version                         OpenCL C 2.0 
  Device Type                                     GPU
  Device Board Name (AMD)                         Radeon Vega Frontier Edition
  Device PCI-e ID (AMD)                           0x6863
  Device Topology (AMD)                           PCI-E, 0000:2b:00.0
  Device Profile                                  FULL_PROFILE
  Device Available                                Yes
  Compiler Available                              Yes
  Linker Available                                Yes
  Max compute units                               64
  SIMD per compute unit (AMD)                     4
  SIMD width (AMD)                                16
  SIMD instruction width (AMD)                    1
  Max clock frequency                             1600MHz
  Graphics IP (AMD)                               9.0
  Device Partition                                (core)
    Max number of sub-devices                     64
    Supported partition types                     None
    Supported affinity domains                    (n/a)
  Max work item dimensions                        3
  Max work item sizes                             1024x1024x1024
  Max work group size                             256
  Preferred work group size (AMD)                 256
  Max work group size (AMD)                       1024
  Preferred work group size multiple (kernel)     64
  Wavefront width (AMD)                           64
  Preferred / native vector sizes                 
    char                                                 4 / 4       
    short                                                2 / 2       
    int                                                  1 / 1       
    long                                                 1 / 1       
    half                                                 1 / 1        (cl_khr_fp16)
    float                                                1 / 1       
    double                                               1 / 1        (cl_khr_fp64)
  Half-precision Floating-point support           (cl_khr_fp16)
    Denormals                                     No
    Infinity and NANs                             No
    Round to nearest                              No
    Round to zero                                 No
    Round to infinity                             No
    IEEE754-2008 fused multiply-add               No
    Support is emulated in software               No
  Single-precision Floating-point support         (core)
    Denormals                                     Yes
    Infinity and NANs                             Yes
    Round to nearest                              Yes
    Round to zero                                 Yes
    Round to infinity                             Yes
    IEEE754-2008 fused multiply-add               Yes
    Support is emulated in software               No
    Correctly-rounded divide and sqrt operations  Yes
  Double-precision Floating-point support         (cl_khr_fp64)
    Denormals                                     Yes
    Infinity and NANs                             Yes
    Round to nearest                              Yes
    Round to zero                                 Yes
    Round to infinity                             Yes
    IEEE754-2008 fused multiply-add               Yes
    Support is emulated in software               No
  Address bits                                    64, Little-Endian
  Global memory size                              17163091968 (15.98GiB)
  Global free memory (AMD)                        16760832 (15.98GiB) 16760832 (15.98GiB)
  Global memory channels (AMD)                    64
  Global memory banks per channel (AMD)           4
  Global memory bank width (AMD)                  256 bytes
  Error Correction support                        No
  Max memory allocation                           14588628168 (13.59GiB)
  Unified memory for Host and Device              No
  Shared Virtual Memory (SVM) capabilities        (core)
    Coarse-grained buffer sharing                 Yes
    Fine-grained buffer sharing                   Yes
    Fine-grained system sharing                   No
    Atomics                                       No
  Minimum alignment for any data type             128 bytes
  Alignment of base address                       1024 bits (128 bytes)
  Preferred alignment for atomics                 
    SVM                                           0 bytes
    Global                                        0 bytes
    Local                                         0 bytes
  Max size for global variable                    14588628168 (13.59GiB)
  Preferred total size of global vars             17163091968 (15.98GiB)
  Global Memory cache type                        Read/Write
  Global Memory cache size                        16384 (16KiB)
  Global Memory cache line size                   64 bytes
  Image support                                   Yes
    Max number of samplers per kernel             26723
    Max size for 1D images from buffer            134217728 pixels
    Max 1D or 2D image array size                 8192 images
    Base address alignment for 2D image buffers   256 bytes
    Pitch alignment for 2D image buffers          256 pixels
    Max 2D image size           Click to expand!                  16
  Max active pipe reservations                    16
  Max pipe packet size                            1703726280 (1.587GiB)
  Local memory type                               Local
  Local memory size                               65536 (64KiB)
  Local memory size per CU (AMD)                  65536 (64KiB)
  Local memory banks (AMD)                        32
  Max number of constant args                     8
  Max constant buffer size                        14588628168 (13.59GiB)
  Preferred constant buffer size (AMD)            16384 (16KiB)
  Max size of kernel argument                     1024
  Queue properties (on host)                      
    Out-of-order execution                        No
    Profiling                                     Yes
  Queue properties (on device)                    
    Out-of-order execution                        Yes
    Profiling                                     Yes
    Preferred size                                262144 (256KiB)
    Max size                                      8388608 (8MiB)
  Max queues on device                            1
  Max events on device                            1024
  Prefer user sync for interop                    Yes
  Number of P2P devices (AMD)                     0
  Profiling timer resolution                      1ns
  Profiling timer offset since Epoch (AMD)        0ns (Wed Dec 31 18:00:00 1969)
  Execution capabilities                          
    Run OpenCL kernels                            Yes
    Run native kernels                            No
    Thread trace supported (AMD)                  No
    Number of async queues (AMD)                  8
    Max real-time compute queues (AMD)            8
    Max real-time compute units (AMD)             64
  printf() buffer size                            4194304 (4MiB)
  Built-in kernels                                (n/a)
  Device Extensions                               cl_khr_fp64 cl_khr_global_int32_base_atomics cl_khr_global_int32_extended_atomics cl_khr_local_int32_base_atomics cl_khr_local_int32_extended_atomics cl_khr_int64_base_atomics cl_khr_int64_extended_atomics cl_khr_3d_image_writes cl_khr_byte_addressable_store cl_khr_fp16 cl_khr_gl_sharing cl_amd_device_attribute_query cl_amd_media_ops cl_amd_media_ops2 cl_khr_image2d_from_buffer cl_khr_subgroups cl_khr_depth_images cl_amd_copy_buffer_p2p cl_amd_assembly_program 

NULL platform behavior
  clGetPlatformInfo(NULL, CL_PLATFORM_NAME, ...)  AMD Accelerated Parallel Processing
  clGetDeviceIDs(NULL, CL_DEVICE_TYPE_ALL, ...)   Success [AMD]
  clCreateContext(NULL, ...) [default]            Success [AMD]
  clCreateContextFromType(NULL, CL_DEVICE_TYPE_DEFAULT)  Success (1)
    Platform Name                                 AMD Accelerated Parallel Processing
    Device Name                                   gfx900:xnack-
  clCreateContextFromType(NULL, CL_DEVICE_TYPE_CPU)  No devices found in platform
  clCreateContextFromType(NULL, CL_DEVICE_TYPE_GPU)  Success (1)
    Platform Name                                 AMD Accelerated Parallel Processing
    Device Name                                   gfx900:xnack-
  clCreateContextFromType(NULL, CL_DEVICE_TYPE_ACCELERATOR)  No devices found in platform
  clCreateContextFromType(NULL, CL_DEVICE_TYPE_CUSTOM)  No devices found in platform
  clCreateContextFromType(NULL, CL_DEVICE_TYPE_ALL)  Success (1)
    Platform Name                                 AMD Accelerated Parallel Processing
    Device Name                                   gfx900:xnack-

ICD loader properties
  ICD loader Name                                 OpenCL ICD Loader
  ICD loader Vendor                               OCL Icd free software
  ICD loader Version                              2.2.14
  ICD loader Profile                              OpenCL 3.0
```

</details>