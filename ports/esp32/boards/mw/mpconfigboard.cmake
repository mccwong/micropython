// copy from generic-OTA
// merge with generic-spiRAM


set(SDKCONFIG_DEFAULTS
    boards/sdkconfig.base
    boards/sdkconfig.ble
    boards/sdkconfig.spiram             // from spiram
    boards/GENERIC_OTA/sdkconfig.board  // from OTA
)

if(NOT MICROPY_FROZEN_MANIFEST)
    set(MICROPY_FROZEN_MANIFEST ${MICROPY_PORT_DIR}/boards/manifest.py)
endif()


