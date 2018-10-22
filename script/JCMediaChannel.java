package com.juphoon.cloud;

import android.support.annotation.IntDef;
import android.support.annotation.StringDef;

import java.lang.annotation.Retention;
import java.lang.annotation.RetentionPolicy;
import java.util.List;
import java.util.Map;

/**
 * 媒体频道模块，类似音视频频道的概念，可以通过频道号加入此频道，从而进行音视频通话
 *
 * @author juphoon
 */
public abstract class JCMediaChannel {

    static final String TAG = JCMediaChannel.class.getSimpleName();

    /**
     * 区域
     */
    @IntDef({REGION_CHINA, REGION_OTHER})
    @Retention(RetentionPolicy.SOURCE)
    public @interface Region {
    }

    /**
     * 中国
     */
    public static final int REGION_CHINA = 0;
    /**
     * 其他区域
     */
    public static final int REGION_OTHER = 100;

    /**
     * 频道加入失败和离开原因
     */
    @IntDef({REASON_NONE, REASON_NOT_LOGIN, REASON_TIMEOUT, REASON_NETWORK, REASON_CALL_FUNCTION_ERROR,
            REASON_ALREADY_JOINED, REASON_KICKED, REASON_OFFLINE, REASON_QUIT, REASON_OVER, REASON_FULL,
            REASON_INVALID_PASSWORD, REASON_OTHER})
    @Retention(RetentionPolicy.SOURCE)
    public @interface MediaChannelReason {
    }

    /**
     * 正常
     */
    public static final int REASON_NONE = 0;
    /**
     * 未登录
     */
    public static final int REASON_NOT_LOGIN = 1;
    /**
     * 超时
     */
    public static final int REASON_TIMEOUT = 2;
    /**
     * 网络异常
     */
    public static final int REASON_NETWORK = 3;
    /**
     * 函数调用失败
     */
    public static final int REASON_CALL_FUNCTION_ERROR = 4;
    /**
     * 已加入
     */
    public static final int REASON_ALREADY_JOINED = 5;
    /**
     * 被踢
     */
    public static final int REASON_KICKED = 6;
    /**
     * 掉线
     */
    public static final int REASON_OFFLINE = 7;
    /**
     * 主动离开
     */
    public static final int REASON_QUIT = 8;
    /**
     * 频道关闭
     */
    public static final int REASON_OVER = 9;
    /**
     * 成员满
     */
    public static final int REASON_FULL = 10;
    /**
     * 无效密码
     */
    public static final int REASON_INVALID_PASSWORD = 11;
    /**
     * 其他错误
     */
    public static final int REASON_OTHER = 100;

    /**
     * 视频图像尺寸等级
     */
    @IntDef({PICTURESIZE_NONE, PICTURESIZE_MIN, PICTURESIZE_SMALL, PICTURESIZE_LARGE, PICTURESIZE_MAX})
    @Retention(RetentionPolicy.SOURCE)
    public @interface PictureSize {
    }

    /**
     * 不渲染
     */
    public static final int PICTURESIZE_NONE = 0;
    /**
     * 最小尺寸
     */
    public static final int PICTURESIZE_MIN = 1;
    /**
     * 小尺寸
     */
    public static final int PICTURESIZE_SMALL = 2;
    /**
     * 大尺寸
     */
    public static final int PICTURESIZE_LARGE = 3;
    /**
     * 最大尺寸
     */
    public static final int PICTURESIZE_MAX = 4;

    /**
     * 自身在频道中状态
     */
    @IntDef({STATE_IDLE, STATE_JOINING, STATE_JOINED, STATE_LEAVING})
    @Retention(RetentionPolicy.SOURCE)
    public @interface MediaChannelState {
    }

    /**
     * 空闲状态
     */
    public static final int STATE_IDLE = 0;
    /**
     * 加入中
     */
    public static final int STATE_JOINING = 1;
    /**
     * 已加入
     */
    public static final int STATE_JOINED = 2;
    /**
     * 离开中
     */
    public static final int STATE_LEAVING = 3;

    /**
     * 成员类型
     */
    @IntDef({PARTICIPANT_TYPE_NORMAL, PARTICIPANT_TYPE_PSTN,
            PARTICIPANT_TYPE_WEBRTC})
    @Retention(RetentionPolicy.SOURCE)
    public @interface ParticipantType {
    }

    /**
     * 普通成员
     */
    public static final int PARTICIPANT_TYPE_NORMAL = 0;
    /**
     * PSTN成员
     */
    public static final int PARTICIPANT_TYPE_PSTN = 1;
    /**
     * Webrtc成员
     */
    public static final int PARTICIPANT_TYPE_WEBRTC = 2;

    /**
     * 音量状态
     */
    @IntDef({VOLUME_STATUS_NONE, VOLUME_STATUS_ZERO, VOLUME_STATUS_LOW, VOLUME_STATUS_MID, VOLUME_STATUS_HIGH})
    @Retention(RetentionPolicy.SOURCE)
    public @interface VolumeStatus {
    }

    /**
     * 静音
     */
    public static final int VOLUME_STATUS_NONE = 0;
    /**
     * 无声音
     */
    public static final int VOLUME_STATUS_ZERO = 1;
    /**
     * 低
     */
    public static final int VOLUME_STATUS_LOW = 2;
    /**
     * 中
     */
    public static final int VOLUME_STATUS_MID = 3;
    /**
     * 高
     */
    public static final int VOLUME_STATUS_HIGH = 4;

    /**
     * 会议网络状态
     */
    @IntDef({NET_STATUS_DISCONNECTED, NET_STATUS_VERY_BAD, NET_STATUS_BAD, NET_STATUS_NORMAL, NET_STATUS_GOOD, NET_STATUS_VERY_GOOD})
    @Retention(RetentionPolicy.SOURCE)
    public @interface NetStatus {
    }

    /**
     * 无
     */
    public static final int NET_STATUS_DISCONNECTED = 0;
    /**
     * 非常差
     */
    public static final int NET_STATUS_VERY_BAD = 1;
    /**
     * 差
     */
    public static final int NET_STATUS_BAD = 2;
    /**
     * 一般
     */
    public static final int NET_STATUS_NORMAL = 3;
    /**
     * 好
     */
    public static final int NET_STATUS_GOOD = 4;
    /**
     * 非常好
     */
    public static final int NET_STATUS_VERY_GOOD = 5;

    /**
     * 视频录制状态
     */
    @IntDef({RECORD_STATE_NONE, RECORD_STATE_READY, RECORD_STATE_RUNNING})
    @Retention(RetentionPolicy.SOURCE)
    public @interface RecordState {
    }

    /**
     * 无法进行视频录制
     */
    public static final int RECORD_STATE_NONE = 0;
    /**
     * 可以开启视频录制
     */
    public static final int RECORD_STATE_READY = 1;
    /**
     * 视频录制中
     */
    public static final int RECORD_STATE_RUNNING = 2;

    /**
     * CDN状态
     */
    @IntDef({CDN_STATE_NONE, CDN_STATE_READY, CDN_STATE_RUNNING})
    @Retention(RetentionPolicy.SOURCE)
    public @interface CdnState {
    }

    /**
     * 无法进行Cdn推流
     */
    public static final int CDN_STATE_NONE = 0;
    /**
     * 可以开启Cdn推流
     */
    public static final int CDN_STATE_READY = 1;
    /**
     * Cdn推流中
     */
    public static final int CDN_STATE_RUNNING = 2;

    /**
     * 配置参数
     */
    @StringDef({CONFIG_CAPACITY, CONFIG_SIP_CALLER_NUMBER, CONFIG_SIP_CORE_NETWORK,
            CONFIG_NOTIFY_VOLUME_CHANGE})
    @Retention(RetentionPolicy.SOURCE)
    public @interface ConfigKey {
    }

    /**
     * 设置频道人数
     */
    public static final String CONFIG_CAPACITY = "config_capacity";

    /**
     * 设置 SIP呼叫 主叫号码
     */
    public static final String CONFIG_SIP_CALLER_NUMBER = "config_sip_caller_number";

    /**
     * 设置 SIP呼叫 核心网ID
     */
    public static final String CONFIG_SIP_CORE_NETWORK = "config_sip_core_network";

    /**
     * 设置是否上报音量变化，音量变化会比较频繁，默认为"1"，不需要则设置为"0"
     */
    public static final String CONFIG_NOTIFY_VOLUME_CHANGE = "config_notify_volume_change";

    /**
     * 加入频道参数关键字
     */
    @StringDef({JOIN_PARAM_CDN, JOIN_PARAM_RECORD, JOIN_PARAM_REGION, JOIN_PARAM_PASSWORD,
            JOIN_PARAM_MAX_RESOLUTION})
    @Retention(RetentionPolicy.SOURCE)
    public @interface JoinParam {
    }

    /**
     * cdn地址参数
     */
    public static final String JOIN_PARAM_CDN = "cdn";
    /**
     * 音视频录制参数
     */
    public static final String JOIN_PARAM_RECORD = "record";
    /**
     * 区域参数，只有相同的区域相同的频道ID才能互通
     *
     * @see Region
     */
    public static final String JOIN_PARAM_REGION = "region";
    /**
     * 密码
     */
    public static final String JOIN_PARAM_PASSWORD = "password";
    /**
     * 平滑模式，保证弱网环境下视频流畅
     */
    public static final String JOIN_SMOOTH_MODE= "smoothMode";
    /**
     * 最大分辨率
     */
    public static final String JOIN_PARAM_MAX_RESOLUTION = "maxResolution";

    /**
     * 最大分辨率
     */
    @IntDef({MAX_RESOLUTION_360p, MAX_RESOLUTION_720p, MAX_RESOLUTION_1080p})
    @Retention(RetentionPolicy.SOURCE)
    public @interface MaxResolution {
    }

    /**
     * 最大分辨率 360p
     */
    public static final int MAX_RESOLUTION_360p = 0;
    /**
     * 最大分辨率 720p
     */
    public static final int MAX_RESOLUTION_720p = 1;
    /**
     * 最大分辨率 1080p
     */
    public static final int MAX_RESOLUTION_1080p = 2;

    /**
     * 属性变化标识类
     */
    public class PropChangeParam {
        /**
         * 上传声音是否变化
         */
        public boolean uploadAudio;
        /**
         * 上传视频是否变化
         */
        public boolean uploadVideo;
        /**
         * 输出声音是否变化
         */
        public boolean audioOut;
        /**
         * CDN状态是否变化
         */
        public boolean cdn;
        /**
         * 录制状态是否变化
         */
        public boolean record;
        /**
         * 屏幕分享是否变化
         */
        public boolean screenShare;
        /**
         * 标题是否变化
         */
        public boolean title;
    }

    private static JCMediaChannel sMediaChannel;

    /**
     * 创建 JCMediaChannel 对象
     *
     * @param client      JCClient 对象
     * @param mediaDevice JCMediaDevice 对象
     * @param callback    JCMediaChannelCallback 回调接口，用于接收 JCMediaChannel 相关通知
     * @return 返回 JCMediaChannel 对象
     */
    public static JCMediaChannel create(JCClient client, JCMediaDevice mediaDevice, JCMediaChannelCallback callback) {
        if (sMediaChannel != null) {
            return sMediaChannel;
        }
        sMediaChannel = new JCMediaChannelImpl(client, mediaDevice, callback);
        return sMediaChannel;
    }

    /**
     * 销毁 JCMediaChannel 对象
     */
    public static void destroy() {
        if (sMediaChannel != null) {
            JCClientThreadImpl.getInstance().post(new Runnable() {
                @Override
                public void run() {
                    sMediaChannel.destroyObj();
                    sMediaChannel = null;
                }
            });
        }
    }

    /**
     * 销毁对象
     */
    protected abstract void destroyObj();

    /**
     * 获得频道标识
     *
     * @return 频道标识
     */
    public abstract String getChannelId();

    /**
     * 获得频道密码
     *
     * @return 频道密码
     */
    public abstract String getPassword();

    /**
     * 获得频道号
     *
     * @return 频道号
     */
    public abstract int getChannelNumber();

    /**
     * 返回频道标题
     *
     * @return 频道标题
     */
    public abstract String getTitle();

    /**
     * 返回当前在频道中的状态
     *
     * @return 当前在频道中的状态
     * @see MediaChannelState
     */
    @MediaChannelState
    public abstract int getState();

    /**
     * 获得所有频道中的成员
     *
     * @return 频道成员列表
     */
    public abstract List<JCMediaChannelParticipant> getParticipants();

    /**
     * 是否上传音频数据
     *
     * @return 是否上传音频数据
     */
    public abstract boolean getUploadLocalAudio();

    /**
     * 是否上传视频数据
     *
     * @return 是否上传视频数据
     */
    public abstract boolean getUploadLocalVideo();

    /**
     * 是否音频输出
     *
     * @return 是否音频输出
     */
    public abstract boolean getAudioOutput();

    /**
     * 获取屏幕共享渲染标识
     *
     * @return 屏幕共享渲染标识，频道中没有屏幕共享则返回null
     */
    public abstract String getScreenRenderId();

    /**
     * 获取开启屏幕共享的用户标识
     *
     * @return 开启屏幕共享的用户标识，没有屏幕共享则为null
     */
    public abstract String getScreenUserId();

    /**
     * 获取频录制状态
     *
     * @return 视频录制状态
     * @see RecordState
     */
    @RecordState
    public abstract int getRecordState();

    /**
     * 获得cdn推流状态
     *
     * @return cdn推流状态
     * @see CdnState
     */
    @CdnState
    public abstract int getCdnState();

    /**
     * 设置相关配置参数
     *
     * @param key   配置关键字
     * @param value 参数值
     * @return      返回 true 表示设置成功，false 表示设置失败
     * @see ConfigKey
     */
    public abstract boolean setConfig(@ConfigKey String key, String value);

    /**
     * 获取相关配置参数
     *
     * @param   key 配置关键字, 参见 JCMediaChannelConstants
     * @return  成功返回字符串类型具体值, 失败返回 NULL
     * @see ConfigKey
     */
    public abstract String getConfig(@ConfigKey String key);

    /**
     * 查询频道相关信息，例如是否存在，人数等
     *
     * @param channelId 频道标识
     * @return          返回操作id，与 onQuery 回调中的 operationId 对应
     */
    public abstract int query(String channelId);

    /**
     * 加入频道
     *
     * @param channelId 媒体频道标识
     * @param params    参数，KEY值参考JoinParam，没有则填null
     * @return 返回 true 表示正常执行调用流程，false 表示调用异常
     * @see Region
     * @see MaxResolution
     * @see JoinParam
     */
    public abstract boolean join(String channelId, Map<String, String> params);

    /**
     * 离开频道，当前只支持同时加入一个频道
     *
     * @return 返回 true 表示正常执行调用流程，false 表示调用异常
     */
    public abstract boolean leave();

    /**
     * 关闭频道，所有成员都将被退出
     *
     * @return 返回 true 表示正常执行调用流程，false 表示调用异常
     */
    public abstract boolean stop();

    /**
     * 开启关闭发送本地音频流
     * 1.在频道中将会与服务器进行交互，服务器会更新状态并同步给其他用户
     * 2.未在频道中则标记是否上传音频流，在join时生效
     * 3.建议每次join前设置
     *
     * @param enable 是否开启本地音频流
     * @return 返回 true 表示正常执行调用流程，false 表示调用异常
     */
    public abstract boolean enableUploadAudioStream(boolean enable);

    /**
     * 开启关闭发送本地视频流
     * 1.在会议中将会与服务器进行交互，服务器会更新状态并同步给其他用户
     * 2.未在频道中则标记是否上传视频流，在join时生效
     * 3.建议每次join前设置
     *
     * @param enable 是否开启本地视频流
     * @return 返回 true 表示正常执行调用流程，false 表示调用异常
     */
    public abstract boolean enableUploadVideoStream(boolean enable);

    /**
     * 开启关闭音频输出，可实现静音功能，建议每次join前设置
     *
     * @param enable 是否开启音频输出
     * @return 返回 true 表示正常执行调用流程，false 表示调用异常
     */
    public abstract boolean enableAudioOutput(boolean enable);

    /**
     * 请求频道中其他用户的视频流
     * 当 pictureSize 为 JCMediaChannelPictureSizeNone 时表示关闭请求
     *
     * @param participant   频道中其他成员对象
     * @param pictureSize   视频请求的尺寸类型
     * @return              返回 true 表示正常执行调用流程，false 表示调用异常
     * @see JCMediaChannel.PictureSize
     */
    public abstract boolean requestVideo(JCMediaChannelParticipant participant, @PictureSize int pictureSize);

    /**
     * 请求屏幕共享的视频流
     * 当 pictureSize 为 JCMediaChannelPictureSizeNone 表示关闭请求
     *
     * @param screenUri     屏幕分享uri
     * @param pictureSize   视频请求尺寸类型
     * @return              返回 true 表示正常执行调用流程，false 表示调用异常
     * @see JCMediaChannel.PictureSize
     */
    public abstract boolean requestScreenVideo(String screenUri, @PictureSize int pictureSize);

    /**
     * 开关Cdn推流
     * 在收到 onMediaChannelPropertyChange 回调后检查是否开启
     *
     * @param enable 是否开启Cdn推流
     * @return 返回 true 表示正常执行调用流程，false 表示调用异常
     */
    public abstract boolean enableCdn(boolean enable);

    /**
     * 开关视频录制
     *
     * @param enable 是否开启视频录制
     * @return 返回 true 表示正常执行调用流程，false 表示调用异常
     */
    public abstract boolean enableRecord(boolean enable);

    /**
     * 开关屏幕分享
     *
     * @param enable 是否开启屏幕分享
     * @return 返回 true 表示正常执行调用流程，false 表示调用异常
     */
    public abstract boolean enableScreenShare(boolean enable);

    /**
     * 获取频道成员
     *
     * @param userId 用户唯一标识
     * @return 成员对象
     */
    public abstract JCMediaChannelParticipant getParticipant(String userId);

    /**
     * 获取统计信息，以Json字符串形式返回，其中包含 "Config"， "Network"，"Transport" 和 "Participants" 4个节点
     *
     * @return 统计信息
     */
    public abstract String getStatistics();

    /**
     * 设置频道自定义属性
     *
     * 调用此接口来设置频道自定义属性
     *
     * @param key   属性 key
     * @param value 属性值
     * @return      返回 true 表示正常执行调用流程，false 表示调用异常
     */
    public abstract boolean setCustomProperty(String key, String value);

    /**
     * 获取自定义频道属性
     *
     * 调用此接口来获取频道自定义属性
     *
     * @param key 属性 key
     * @return 属性值
     */
    public abstract String getCustomProperty(String key);

    /**
     * 发送消息
     *
     * @param type     消息类型
     * @param content  消息内容，当 toUserId 不为 null 时，content 不能大于 4k
     * @param toUserId 接收者id，null则发给频道所有人员
     * @return true表示成功，false表示失败
     */
    public abstract boolean sendMessage(String type, String content, String toUserId);

    /**
     * 发送指令<br>
     * <p>
     * 指令名: StartForward	指令作用：请求服务器开始转发音视频<br>
     * 参数格式:{"MtcConfUserUriKey": "用户Uri", "MtcConfMediaOptionKey": "类型"}<br>
     * 用户Uri: 通过调用底层Mtc接口获取 MtcUser.Mtc_UserFormUri(EN_MTC_USER_ID_USERNAME, userId)<br>
     * 类型:  服务器转发分三种 音频、视频、音视频，具体可参考底层mtc_conf.h下的MtcConfMedia的枚举值。<br>
     * 注意1:指令发送成功后会收到 onParticipantUpdate 回调 <br>
     * 举例: {"MtcConfUserUriKey": "[username:justin@sample.cloud.justalk.com]", "MtcConfMediaOptionKey": 3}<br><br>
     * <p>
     * 指令名: StopForward	指令作用：请求服务器停止转发音视频<br>
     * 参数格式:{"MtcConfUserUriKey": "用户URL", "MtcConfMediaOptionKey": "类型"}<br>
     * 用户Uri: 通过调用底层Mtc接口获取 MtcUser.Mtc_UserFormUri(EN_MTC_USER_ID_USERNAME, userId)<br>
     * 类型:  服务器转发分三种 音频、视频、音视频，具体可参考底层mtc_conf.h下的MtcConfMedia的枚举值。<br>
     * 注意1:指令发送成功后会收到 onParticipantUpdate 回调 <br>
     * 举例: {"MtcConfUserUriKey": "[username:justin@sample.cloud.justalk.com]", "MtcConfMediaOptionKey": 3}<br><br>
     * <p>
     * 指令名: ChangeTitle	指令作用：请求修改会议主题<br>
     * 参数格式: {"MtcConfTitleKey":"修改的内容"}<br>
     * 修改的内容: 比如原来主题设置的是"123"，现在改为"321"。<br>
     * 注意1:指令发送成功后会收到 onMediaChannelPropertyChange 回调<br>
     * 注意2:可通过 JCManager.shared.mediaChannel.title 获取主题<br>
     * 举例:{"MtcConfTitleKey": "321"}<br><br>
     * <p>
     * 指令名: SetPartpProp	 指令作用：批量修改成员状态，角色，昵称。<br>
     * 参数格式: {"MtcConfStateKey":1,"MtcConfDisplayNameKey":"1314","MtcConfPartpLstKey":["[username:10086@sample.cloud.justalk.com]"],"MtcConfRoleKey":7}<br>
     * 要修改的成员状态: 具体可参考底层 mtc_conf.h 下的 MtcConfState 的枚举值<br>
     * 要修改的成员角色: 具体可参考底层 mtc_conf.h 下的 MtcConfRole 的枚举值<br>
     * 要修改的成员昵称: 比如"123"<br>
     * 用户Uri:通过调用底层Mtc接口获取 MtcUser.Mtc_UserFormUri(EN_MTC_USER_ID_USERNAME, userId); <br>
     * 注意1:指令发送成功后会收到 onParticipantUpdate 回调 <br>
     * 注意2:MtcConfStateKey、MtcConfDisplayNameKey、MtcConfRoleKey这三个字段，可根据用户想修改哪个值，就在json字符串里面加入哪个。<br>
     * 注意3:MtcConfPartpLstKey 可包含多个用户uri进行批量修改<br>
     * 举例:{"MtcConfStateKey":4,"MtcConfDisplayNameKey":"123","MtcConfPartpLstKey":{"MtcConfUserUriKey":"[username:10086@sample.cloud.justalk.com]","MtcConfStateKey":4},"MtcConfRoleKey":4}<br><br>
     * <p>
     * 指令名：ReplayApplyMode 指令作用：设置推流布局模式<br>
     * 指令参数格式：{"MtcConfCompositeModeKey": 参数值}<br>
     * 参数值：<br>
     * 1 平铺模式,所有视频均分平铺<br>
     * 2 讲台模式,共享为大图,其他视频为小图<br>
     * 3 演讲模式,共享为大图,共享者视频为小图,其他不显示<br>
     * 4 自定义模式,由ReplayApplyLayout指令设置所有视频布局<br>
     * 5 智能模式。<br>
     * 举例：输入指令参数{"MtcConfCompositeModeKey": 2}就是讲台模式<br><br>
     * <p>
     * 指令名：ReplayApplyLayout 指令作用：为多用户设置自定义推流布局<br>
     * 指令参数格式：{[{"MtcConfUserUriKey": "用户uri", "MtcConfPictureSizeKey": 视频尺寸,"MtcConfRectangleKey": 图像矩形的具体方位和长宽}]，...}<br>
     * 用户uri：通过调用底层Mtc接口获取MtcUser.Mtc_UserFormUri((uint)EN_MTC_USER_ID_TYPE.EN_MTC_USER_ID_USERNAME，userId)<br>
     * 视频尺寸：一共5个枚举值，具体枚举值请参考底层mtc_conf.h下的MtcConfPs枚举<br>
     * 图像矩形的具体方位和长宽：这是一个Json格式的Array对象表示这个图像的位置和大小，第一个值是图像左上角的x坐标(0~1)<br>
     * 第二个值是图像左上角的y坐标(0~1)。第三个值是图像的宽(0~1)。第四个值是图像的高(0~1)。比如[0.5,0.5,0.5,0.5]表示图像在右下角长宽是原始屏幕的一半<br>
     * 举例：<br>
     * [{"MtcConfUserUriKey":"[username:zhang@xxxx.cloud.justalk.com]","MtcConfPictureSizeKey":512,"MtcConfRectangleKey":[0.5,0.5,0.5,0.5]}]<br>
     * 表示成员zhang小尺寸的视频在屏幕右下角位置，长宽是原始屏幕的一半<br>
     *
     * @param name  指令名
     * @param param 指令参数
     * @return true表示成功，false表示失败
     */
    public abstract boolean sendCommand(String name, String param);

    /**
     * 邀请Sip用户，一般用于对接落地网关等
     *
     * @param userId    一般为号码
     * @param sipParam  sipParam nil 或者通过 JCMediaChannelUtils.buildSipParam 构造
     * @return          成功返回值 >= 0，失败返回 -1
     */
    public abstract int inviteSipUser(String userId, String sipParam);

    /**
     * 添加回调
     *
     * @param callback 回调对象
     */
    protected abstract void addCallback(JCMediaChannelCallback callback);

    /**
     * 移除回调
     *
     * @param callback 回调对象
     */
    protected abstract void removeCallback(JCMediaChannelCallback callback);

    protected abstract boolean joinEx(String confUri, int role);

}
